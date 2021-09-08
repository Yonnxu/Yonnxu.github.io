package com.SenXuWeather.android.service;


import android.app.AlarmManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.IBinder;
import android.os.SystemClock;
import android.preference.PreferenceManager;

import com.SenXuWeather.android.gson.SuggestBean;
import com.SenXuWeather.android.gson.WeatherBean;
import com.SenXuWeather.android.util.HttpUtil;
import com.google.gson.Gson;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.Response;

public class AutoUpdateService extends Service {

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        updateWeather();
        updateSuggest();
        updateBingPic();
        AlarmManager manager = (AlarmManager) getSystemService(ALARM_SERVICE);
        int anHour = 8 * 60 * 60 * 1000; // 这是8小时的毫秒数
        long triggerAtTime = SystemClock.elapsedRealtime() + anHour;
        Intent i = new Intent(this, AutoUpdateService.class);
        PendingIntent pi = PendingIntent.getService(this, 0, i, 0);
        manager.cancel(pi);
        manager.set(AlarmManager.ELAPSED_REALTIME_WAKEUP, triggerAtTime, pi);
        return super.onStartCommand(intent, flags, startId);
    }

   //更新天气信息

    private void updateWeather(){
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);
        String weatherString = prefs.getString("weather", null);
        if (weatherString != null) {
            // 有缓存时直接解析天气数据
//            Weather weather = Utility.handleWeatherResponse(weatherString);
            final Gson gson = new Gson();
            WeatherBean weatherBean = gson.fromJson(weatherString, WeatherBean.class);
            String weatherName = weatherBean.getResult().getCity();
            String weatherUrl = "http://apis.juhe.cn/simpleWeather/query?city=" + weatherName + "&key=6092a12d08e136afead8bb3c6d9a7084";
            HttpUtil.sendOkHttpRequest(weatherUrl, new Callback() {
                @Override
                public void onResponse(Call call, Response response) throws IOException {
                    String responseText = response.body().string();
                    WeatherBean weather = gson.fromJson(responseText,WeatherBean.class);
                    if (weather != null && "ok".equals(weather.getReason())) {
                        SharedPreferences.Editor editor = PreferenceManager.getDefaultSharedPreferences(AutoUpdateService.this).edit();
                        editor.putString("weather", responseText);
                        editor.apply();
                    }
                }

                @Override
                public void onFailure(Call call, IOException e) {
                    e.printStackTrace();
                }
            });
        }
    }


    private void updateSuggest(){
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);
        String suggestString = prefs.getString("suggest", null);
        if (suggestString != null) {
            final Gson gson = new Gson();
            SuggestBean suggestBean = gson.fromJson(suggestString, SuggestBean.class);
            String suggestName = suggestBean.getResult().getCity();
            String suggestUrl = "http://apis.juhe.cn/simpleWeather/life?city=" + suggestName + "&key=6092a12d08e136afead8bb3c6d9a7084";
            HttpUtil.sendOkHttpRequest(suggestUrl, new Callback() {
                @Override
                public void onResponse(Call call, Response response) throws IOException {
                    String responseText = response.body().string();
                    SuggestBean suggest = gson.fromJson(responseText,SuggestBean.class);
                    if (suggest != null && "ok".equals(suggest.getReason())) {
                        SharedPreferences.Editor editor = PreferenceManager.getDefaultSharedPreferences(AutoUpdateService.this).edit();
                        editor.putString("suggest", responseText);
                        editor.apply();
                    }
                }

                @Override
                public void onFailure(Call call, IOException e) {
                    e.printStackTrace();
                }
            });
        }
    }




    //更新每日一图

    private void updateBingPic() {
        String requestBingPic = "http://guolin.tech/api/bing_pic";
        HttpUtil.sendOkHttpRequest(requestBingPic, new Callback() {
            @Override
            public void onResponse(Call call, Response response) throws IOException {
                String bingPic = response.body().string();
                SharedPreferences.Editor editor = PreferenceManager.getDefaultSharedPreferences(AutoUpdateService.this).edit();
                editor.putString("bing_pic", bingPic);
                editor.apply();
            }

            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }
        });
    }

}
