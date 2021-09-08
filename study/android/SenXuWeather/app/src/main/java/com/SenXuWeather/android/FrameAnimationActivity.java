package com.SenXuWeather.android;
import android.content.Intent;
import android.graphics.drawable.AnimationDrawable;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;


public class FrameAnimationActivity extends AppCompatActivity{
    private ImageView img_frame;
    private Button btn_start;
    private AnimationDrawable animationDrawable;//逐帧动画对象

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //加载布局文件
        setContentView(R.layout.animat);
        initView();
    }

    private void initView() {
        img_frame = (ImageView) findViewById(R.id.img_frame);
        btn_start = (Button) findViewById(R.id.btn_start);

        //通过ImageView控件的background属性获取逐帧动画对象
        animationDrawable=(AnimationDrawable) img_frame.getBackground();
        animationDrawable.start();

        btn_start.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent=new Intent(FrameAnimationActivity.this,WeatherActivity.class);
                startActivity(intent);
                toast();
                finish();
            }
        });


    }

    private void toast()
    {

        Toast toastCustom = new Toast(getApplicationContext());
        LayoutInflater inflater=LayoutInflater.from(FrameAnimationActivity.this);
        View view = inflater.inflate(R.layout.toast,null);
        ImageView imageView=view.findViewById(R.id.iv_toast);
        TextView textView=view.findViewById(R.id.tv_toast);

        toastCustom.setGravity(Gravity.CENTER_HORIZONTAL|Gravity.BOTTOM , 0, 20);  //设置显示位置
        textView.setText("Welcome");
        imageView.setImageResource(R.mipmap.welcome);
        toastCustom.setView(view);
        toastCustom.setDuration(Toast.LENGTH_LONG);
        toastCustom.show();
    }
}
