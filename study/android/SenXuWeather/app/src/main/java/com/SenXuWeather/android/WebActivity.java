package com.SenXuWeather.android;


import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Intent;
import android.os.Build;
import android.os.Bundle;

import android.view.KeyEvent;
import android.webkit.WebResourceRequest;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import androidx.annotation.RequiresApi;

import static com.SenXuWeather.android.R.layout.web_view;

public class WebActivity extends Activity {
    private WebView mBtnWv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(web_view);
        initView();

    }

    @SuppressLint("SetJavaScriptEnabled")
    private void initView() {
        mBtnWv = (WebView) findViewById(R.id.mBtnWv);
        Intent intent =getIntent();
        String context = intent.getStringExtra("et_context");

        //设置WebView属性,运行执行js脚本
        mBtnWv.getSettings().setJavaScriptEnabled(true);

        mBtnWv.setWebViewClient(new MyWebViewClient());

        //调用loadUrl方法为WebView加载网页的URL
        mBtnWv.loadUrl("https://m.baidu.com/ssid=ac5e534b59d8bcc8413333b1f6/s?word=" + context+
                "&ts=2062352&t_kt=0&ie=utf-8&rsv_iqid=4222825077&rsv_t=eb51LRnjBeDsnw6KgTmNFA34Cd6BXzCjzWDfr5T6ly5040%252FNeJmL&sa=ib&rsv_pq=4222825077&rsv_sug4=5153&ss=110&tj=1&inputT=3028&sugid=2223152531520898889");

    }

    static class MyWebViewClient extends WebViewClient
    {
        @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
        @Override
        //页面跳转时调用此方法                                       网络资源请求
        public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request)
        {
            //在当前webView加载
            view.loadUrl(request.getUrl().toString());
            return true;
        }
    }

    public boolean onKeyDown(int keyCode, KeyEvent event)
    {
        //如果按得是返回键 且可以返回.
        if (keyCode == KeyEvent.KEYCODE_BACK && mBtnWv.canGoBack())
        {
            mBtnWv.goBack();
            //此事件处理完成，无需再处理
            return true;
        }
        return super.onKeyDown(keyCode, event);
    }

}
