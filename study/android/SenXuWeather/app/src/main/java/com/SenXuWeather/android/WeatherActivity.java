package com.SenXuWeather.android;


import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Build;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import com.SenXuWeather.android.gson.SuggestBean;
import com.bumptech.glide.Glide;
import com.SenXuWeather.android.gson.WeatherBean;
import com.SenXuWeather.android.service.AutoUpdateService;
import com.SenXuWeather.android.util.HttpUtil;
import com.google.gson.Gson;

import java.io.IOException;
import java.util.List;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.Response;

public class WeatherActivity extends AppCompatActivity {

    public DrawerLayout drawerLayout;

    public SwipeRefreshLayout swipeRefresh;

    private ScrollView weatherLayout;

    private Button navButton;

    private TextView titleCity;

    private TextView titleUpdateTime;

    private TextView degreeText;

    private TextView weatherInfoText;

    private LinearLayout forecastLayout;

    private TextView aqiText;

    private TextView tv_dum;

    private TextView comfortText;

    private TextView carWashText;

    private TextView sportText;

    private ImageView bingPicImg;

    private String weatherName;

    private Button btnsearch;

    private EditText et_context;

    private String context;

    @SuppressLint("SetJavaScriptEnabled")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (Build.VERSION.SDK_INT >= 21) {
            View decorView = getWindow().getDecorView();
            decorView.setSystemUiVisibility(View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                    | View.SYSTEM_UI_FLAG_LAYOUT_STABLE);
            getWindow().setStatusBarColor(Color.TRANSPARENT);
        }
        setContentView(R.layout.activity_weather);
        // 初始化各控件
        bingPicImg = (ImageView) findViewById(R.id.bing_pic_img);
        weatherLayout = (ScrollView) findViewById(R.id.weather_layout);
        titleCity = (TextView) findViewById(R.id.title_city);
        titleUpdateTime = (TextView) findViewById(R.id.title_update_time);
        degreeText = (TextView) findViewById(R.id.degree_text);
        weatherInfoText = (TextView) findViewById(R.id.weather_info_text);
        forecastLayout = (LinearLayout) findViewById(R.id.forecast_layout);
        aqiText = (TextView) findViewById(R.id.aqi_text);
        tv_dum = (TextView) findViewById(R.id.tv_dum);
        comfortText = (TextView) findViewById(R.id.comfort_text);
        carWashText = (TextView) findViewById(R.id.car_wash_text);
        sportText = (TextView) findViewById(R.id.sport_text);
        swipeRefresh = (SwipeRefreshLayout) findViewById(R.id.swipe_refresh);
        swipeRefresh.setColorSchemeResources(R.color.colorPrimary);
        drawerLayout = (DrawerLayout) findViewById(R.id.drawer_layout);
        navButton = (Button) findViewById(R.id.nav_button);
        btnsearch = (Button) findViewById(R.id.btn_search);

        et_context=findViewById(R.id.et_context);
        //用LayoutInflater加载布局
        LayoutInflater factory = LayoutInflater.from(WeatherActivity.this);
        //获取dialog布局文件获取View
        View textEntryView = factory.inflate(R.layout.web_view, null);
        // 通过textEntryView来获取控件
        final WebView web = (WebView) textEntryView.findViewById(R.id.mBtnWv);

        btnsearch.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                if (!(context=et_context.getText().toString()).isEmpty()){
                    Intent intent = new Intent(WeatherActivity.this, WebActivity.class);
                    intent.putExtra("et_context", context);
                    startActivity(intent);

                   }else{
                    Toast.makeText(WeatherActivity.this, "请输入内容", Toast.LENGTH_SHORT).show();
                }
               }
        });

        final SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);
        SharedPreferences preferences = getSharedPreferences("cityData",MODE_PRIVATE);
        String weatherString = prefs.getString("weather", null);
        String suggestString = prefs.getString("suggest", null);
        weatherName = preferences.getString("city",null);
        Log.i("TAG",weatherName+"-----start------");
        if (weatherString != null && suggestString != null &&weatherString == weatherName && suggestString ==weatherName) {
            // 有缓存时直接解析天气数据
            Gson gson = new Gson();
            showWeatherInfo(gson.fromJson(weatherString, WeatherBean.class));
            showSuggestInfo(gson.fromJson(suggestString, SuggestBean.class));
        } else {
            // 无缓存时去服务器查询天气
            weatherLayout.setVisibility(View.INVISIBLE);
            requestWeather(weatherName);
            requestSuggest(weatherName);
        }
        swipeRefresh.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                SharedPreferences preferences = getSharedPreferences("cityData",MODE_PRIVATE);
                String weatherString = prefs.getString("weather", null);
                String suggestString = prefs.getString("suggest", null);
                weatherName = preferences.getString("city",null);
                Log.i("TAG",weatherName+"-----刷新--------");
                requestWeather(weatherName);
                requestSuggest(weatherName);
            }
        });
        navButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                drawerLayout.openDrawer(GravityCompat.START);
            }
        });
        String bingPic = prefs.getString("bing_pic", null);
        if (bingPic != null) {
            Glide.with(this).load(bingPic).into(bingPicImg);
        } else {
            loadBingPic();
        }
    }

    public void requestSuggest(final String weatherId){
        Log.i("TAG", "requestWeather: "+weatherId+"Suggest----------");
        String suggestUrl = "http://apis.juhe.cn/simpleWeather/life?city=" + weatherId + "&key=6092a12d08e136afead8bb3c6d9a7084";
        HttpUtil.sendOkHttpRequest(suggestUrl, new Callback() {
            @Override
            public void onResponse(Call call, Response response) throws IOException {
                //服务器返回的字符串
                final String responsesuggest = response.body().string();
                Gson gson = new Gson();
                final SuggestBean suggestBean=gson.fromJson(responsesuggest, SuggestBean.class);
                Log.i("TAG",suggestBean.getReason());
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        if (suggestBean != null && "查询成功!".equals(suggestBean.getReason())) {
                            SharedPreferences.Editor editorsuggest = PreferenceManager.getDefaultSharedPreferences(WeatherActivity.this).edit();
                            editorsuggest.putString("suggest", responsesuggest);
                            editorsuggest.apply();
                            showSuggestInfo(suggestBean);
                            Toast.makeText(WeatherActivity.this, "查询成功", Toast.LENGTH_SHORT).show();
                        } else {
                            Toast.makeText(WeatherActivity.this, "Fail：超过每日允许次数", Toast.LENGTH_SHORT).show();
                        }
                        //停止刷新的方法
                        swipeRefresh.setRefreshing(false);
                    }

                });
            }

            @Override
            public void onFailure(Call call, IOException e) {
                //判断是否失败
                e.printStackTrace();
                // 通过runOnUiThread()方法回到主线程处理逻辑
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        Toast.makeText(WeatherActivity.this, "获取天气信息失败", Toast.LENGTH_SHORT).show();
                        swipeRefresh.setRefreshing(false);
                    }
                });
            }
        });
    }

    //根据天气id请求城市天气信息

    public void requestWeather(final String weatherId) {
        Log.i("TAG", "requestWeather: "+weatherId+"Weather----------");
        String weatherUrl = "http://apis.juhe.cn/simpleWeather/query?city=" + weatherId + "&key=6092a12d08e136afead8bb3c6d9a7084";
        HttpUtil.sendOkHttpRequest(weatherUrl, new Callback() {
            @Override
            public void onResponse(Call call, Response response) throws IOException {
                //服务器返回的字符串
                final String responseText = response.body().string();
                //final Weather weather = Utility.handleWeatherResponse(responseText);
                Gson gson = new Gson();
                //把weatherbean转化为Json数据
                final WeatherBean weatherbean=gson.fromJson(responseText, WeatherBean.class);
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        if (weatherbean != null && "查询成功!".equals(weatherbean.getReason())) {
                            SharedPreferences.Editor editor = PreferenceManager.getDefaultSharedPreferences(WeatherActivity.this).edit();
                            editor.putString("weather", responseText);
                            editor.apply();
                           // weatherName = weather.basic.weatherId;
                            showWeatherInfo(weatherbean);
                            Toast.makeText(WeatherActivity.this, "查询成功", Toast.LENGTH_SHORT).show();
                        } else {
                            Toast.makeText(WeatherActivity.this, "Fail：超过每日允许次数", Toast.LENGTH_SHORT).show();
                        }
                        swipeRefresh.setRefreshing(false);
                    }
                });
            }

            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
                // 通过runOnUiThread()方法回到主线程处理逻辑
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        Toast.makeText(WeatherActivity.this, "获取天气信息失败", Toast.LENGTH_SHORT).show();
                        swipeRefresh.setRefreshing(false);
                    }
                });
            }
        });
        loadBingPic();
    }

    @SuppressLint("SetTextI18n")
    private void showSuggestInfo(SuggestBean suggestBean) {
            comfortText.setText("舒适度: " +suggestBean.getResult().getLife().getShushidu().getDes());
            carWashText.setText("洗车: " + suggestBean.getResult().getLife().getXiche().getDes());
            sportText.setText("运动: " + suggestBean.getResult().getLife().getYundong().getDes());
    }

    //加载每日一图

    private void loadBingPic() {
        String requestBingPic = "http://guolin.tech/api/bing_pic";
        HttpUtil.sendOkHttpRequest(requestBingPic, new Callback() {
            @Override
            public void onResponse(Call call, Response response) throws IOException {
                final String bingPic = response.body().string();
                SharedPreferences.Editor editor = PreferenceManager.getDefaultSharedPreferences(WeatherActivity.this).edit();
                editor.putString("bing_pic", bingPic);
                editor.apply();
                // 通过runOnUiThread()方法回到主线程处理逻辑
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        Glide.with(WeatherActivity.this).load(bingPic).into(bingPicImg);
                    }
                });
            }

            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }
        });
    }


    //处理并展示Weather实体类中的数据
    @SuppressLint("SetTextI18n")
    private void showWeatherInfo(WeatherBean weatherBean) {
        String cityName = weatherBean.getResult().getCity();
        List<WeatherBean.ResultBean.FutureBean> futureBeans = weatherBean.getResult().getFuture();
        String updateTime = futureBeans.get(0).getDate();
        String degree = weatherBean.getResult().getRealtime().getTemperature() + "℃";
        String weatherInfo = weatherBean.getResult().getRealtime().getInfo();
        titleCity.setText(cityName);
        titleUpdateTime.setText(updateTime);
        degreeText.setText(degree);
        weatherInfoText.setText(weatherInfo);
        forecastLayout.removeAllViews();
        for (int i=1;i<weatherBean.getResult().getFuture().size();i++) {
            View view = LayoutInflater.from(this).inflate(R.layout.forecast_item, forecastLayout, false);
            TextView dateText = (TextView) view.findViewById(R.id.date_text);
            TextView infoText = (TextView) view.findViewById(R.id.info_text);
            TextView maxText = (TextView) view.findViewById(R.id.max_text);
            TextView minText = (TextView) view.findViewById(R.id.min_text);
            dateText.setText(weatherBean.getResult().getFuture().get(i).getDate());
            infoText.setText(weatherBean.getResult().getFuture().get(i).getWeather());
            maxText.setText(weatherBean.getResult().getFuture().get(i).getTemperature().substring(weatherBean.getResult().getFuture().get(i).getTemperature().indexOf("/")+1));
            minText.setText(weatherBean.getResult().getFuture().get(i).getTemperature().substring(weatherBean.getResult().getFuture().get(i).getTemperature().indexOf("/")-1,weatherBean.getResult().getFuture().get(i).getTemperature().indexOf("/"))+"°C");
//            Log.i("TAG","min:"+weatherBean.getResult().getFuture().get(i).getTemperature().substring(weatherBean.getResult().getFuture().get(i).getTemperature().indexOf("\\")+1,weatherBean.getResult().getFuture().get(i).getTemperature().indexOf("\\")+2));
            forecastLayout.addView(view);
        }
        tv_dum.setText(weatherBean.getResult().getRealtime().getHumidity());


        if (weatherBean.getResult().getRealtime().getAqi() != null) {
            int aqi = 0;
            try {
                aqi = Integer.parseInt(weatherBean.getResult().getRealtime().getAqi());
            } catch (Exception e) {
                e.printStackTrace();
            }
            aqiText.setText(weatherBean.getResult().getRealtime().getAqi());
            aqiText.setTextSize(40);

            if (aqi == 0) aqiText.setTextColor(Color.WHITE);
            else if (aqi < 50) aqiText.setTextColor(getResources().getColor(R.color.a50));
            else if (aqi < 100) aqiText.setTextColor(getResources().getColor(R.color.a100));
            else if (aqi < 150) aqiText.setTextColor(getResources().getColor(R.color.a150));
            else if (aqi < 200) aqiText.setTextColor(getResources().getColor(R.color.a200));
            else if (aqi < 300) aqiText.setTextColor(getResources().getColor(R.color.a300));
            else if (aqi > 300) aqiText.setTextColor(getResources().getColor(R.color.a300up));

        }else {
            aqiText.setTextColor(Color.WHITE);
            aqiText.setText("暂无数据");
            aqiText.setTextSize(25);
            aqiText.setSingleLine();
        }
        weatherLayout.setVisibility(View.VISIBLE);
        Intent intent = new Intent(this, AutoUpdateService.class);
        //启动service
        startService(intent);
    }

    }