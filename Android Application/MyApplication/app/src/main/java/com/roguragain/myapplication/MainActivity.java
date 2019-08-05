package com.roguragain.myapplication;

import android.annotation.SuppressLint;
import android.app.Dialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Build;
import android.provider.DocumentsContract;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Layout;
import android.util.Log;
import android.view.KeyEvent;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.ConsoleMessage;
import android.webkit.JavascriptInterface;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ArrayAdapter;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.xmlpull.v1.XmlPullParser;

import java.io.Console;
import java.net.URLConnection;
import java.util.ArrayList;


public class MainActivity extends AppCompatActivity {
    WebView webView ;

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {

        if(event.getAction()==KeyEvent.ACTION_DOWN){
            switch (keyCode){
                case KeyEvent.KEYCODE_BACK:
                    if(webView.canGoBack()==true){
                        webView.goBack();
                    }
                    else {
                        finish();
                    }
                    return true;
            }
        }

        return super.onKeyDown(keyCode, event);
    }

    String run = "function check_nepali(title)" +
            "{" +
            "    var a = 0;" +
            "    for(var i=0;i<title.length;i++)" +
            "    {" +
            "        var int_of_nep = title[i].charCodeAt(0);" +
            "        if(int_of_nep > 2324)" +
            "        {" +
            "            a ++;" +
            "        }" +
            "    }" +
            "    if (a> title.length/3)" +
            "    {" +
            "        return true;" +
            "    }" +
            "    return false;" +
            "}" +
            "" +
            "" +
            "function createRow(title,post){" +

            "var p = post.getElementsByClassName('_2pis');" +
            "var a = check_nepali(title);"+
            "if(p[0].getElementsByClassName('this-is-my-class').length===0 && a==true){" +
            "var item  = document.createElement('div');" +
            "item.className='this-is-my-class';" +
            "item.id='my-id';" +
            "item.onclick=function(){ob.getData(this.querySelector('img').id);};" +

            "item.height=50;item.width=50;" +

            "item.innerHTML='<img src=\"https://i.imgur.com/znVk04Z.png\" class=\"this-is-my-image\" id=\"\'+title+\'\" height=\"25px\" width=\"25px\" style=\"float:right;display:inline;margin-right:5px\">';"+
            "p[0].appendChild(item);" +
            "}" +
            "}" +
       //     "setInterval(function() {"+
            "try{"+
            "var posts = window.document.querySelectorAll('article');}" +
            "catch(err){alert(err.message)}" +
            "for(var i=0;i<posts.length;i++){" +
            "try" +
            "{" +
            "var post = posts[i];" +
            "var dat = post.querySelector('._2w79');" +
            "data = dat.querySelector('span').innerText;" +
            "if(data){" +
            "createRow(data,post);"+

            "}" +
            "}catch(err){}}"+
            ""+

            ""
         //   "},5000);"

            ;
    @SuppressLint({"ClickableViewAccessibility", "JavascriptInterface"})
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final String[] theUrl = new String[1];
        webView = findViewById(R.id.webview);
        MyJavaScriptInterface myJavaScriptInterface = new MyJavaScriptInterface(this,webView);


        //final WebView webView = new WebView(this);

        webView.getSettings().setRenderPriority(WebSettings.RenderPriority.HIGH);
        webView.getSettings().setAllowUniversalAccessFromFileURLs(true);
        webView.addJavascriptInterface(myJavaScriptInterface,"ob");
        webView.getSettings().setCacheMode(WebSettings.LOAD_DEFAULT);


        //webView.evaluateJavascript(run, null);
        //to show the loaded site on the activity rather than default browser
        webView.setWebViewClient(new WebViewClient(){
            @Override
            public void onPageFinished(WebView view, String url) {
                super.onPageFinished(view, url);
                //view.loadUrl("javascript:"+run);
                //view.loadUrl("javascript:"+run);
                //view.evaluateJavascript(run, null);


            }

            @Override
            public void onLoadResource(WebView view, String url) {
                view.loadUrl("javascript:"+run);
                super.onLoadResource(view, url);

            }

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                //Log.i("iiii","url changed");
                view.loadUrl(url);
                return false;
            }

            @Override
            public void onReceivedError (WebView view, int errorCode, String description, String failingUrl){
               // Log.d("ERROR", "onReceivedError : " +failingUrl + "::" + description);
            }



            @Override
            public void onPageStarted(WebView view, String url, Bitmap favicon) {
                super.onPageStarted(view, url, favicon);
             //   Log.d("URL",url);
            }


        });
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
            webView.setLayerType(View.LAYER_TYPE_HARDWARE, null);
        } else {
            webView.setLayerType(View.LAYER_TYPE_SOFTWARE, null);
        }

        webView.getSettings().setJavaScriptEnabled(true);
        //webView.setWebChromeClient(new WebChromeClient());




        //webView.getSettings().setUserAgentString("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36");






        webView.loadUrl("http://m.facebook.com/kantipuronline");
        Log.d("NOW URL",webView.getUrl());




    }



    }


class MyJavaScriptInterface
{
    ArrayList<news> arrayListNews = null;
    JSONArray links;
    WebView webView;
    Context mctx;
    String annapurna = "AnnapurnaPost";
    String kantipur = "ekantipur";
    String onlineKhabar = "OnlineKhabar";
    String nagarik = "Nagarik_news";


    public MyJavaScriptInterface(Context context, WebView webView) {
        mctx = context;
        this.webView = webView;
    }

    @JavascriptInterface
    public String getData(String title) throws JSONException {
        Log.d("JSON",title);
        String url = "http://3.81.160.151:8000/news/"+title;
        String json = UrlConnection.getNewsJson(url);
        Log.d("JSON",json);
        final ArrayList<news> arrayListNews = new ArrayList<>();
        final AlertDialog.Builder ab = new AlertDialog.Builder(mctx);
        ab.setTitle("News");
        ArrayList<String> items = new ArrayList<String>();
        //ArrayAdapter<String> items = new ArrayAdapter<String>(mctx,0);



        if(json.isEmpty()){
            return null;
        }
        try {
            JSONObject jsonObject = new JSONObject(json);
            links = jsonObject.getJSONArray("result");



        } catch (JSONException e) {
            e.printStackTrace();
        }
        try {

            for(int i=0;i<links.length();i++)
            {
                JSONObject link = (JSONObject) links.get(i);
                news n1 = new news(link.get("title").toString(),link.get("link").toString(),link.get("site").toString());
                Log.i("bews",n1.toString());
                items.add(link.get("title").toString());
                arrayListNews.add(n1);
            }

//            if(links.get(onlineKhabar)!=null){
//                JSONArray newsContent = (JSONArray) links.get(onlineKhabar);
//                news n1 = new news(newsContent.get(1).toString(),newsContent.get(0).toString(),onlineKhabar);
//                items.add(newsContent.get(1).toString());
//                arrayListNews.add(n1);
//
//            }
        }catch (JSONException e)
        {
            e.printStackTrace();
        }

//        try {
//            if (links.get(annapurna)!=null){
//                JSONArray newsContent = (JSONArray) links.get(annapurna);
//                news n1 = new news(newsContent.get(1).toString(),newsContent.get(0).toString(),annapurna);
//                items.add(newsContent.get(1).toString());
//                arrayListNews.add(n1);
//
//            }
//        }catch (JSONException e){
//            e.printStackTrace();
//        }
//        try {
//            if (links.get(kantipur)!=null){
//                JSONArray newsContent = (JSONArray) links.get(kantipur);
//                news n1 = new news(newsContent.get(1).toString(),newsContent.get(0).toString(),kantipur);
//                items.add(newsContent.get(1).toString());
//                arrayListNews.add(n1);
//
//            }
//        }catch (JSONException e){
//            e.printStackTrace();
//        }
//        try {
//            if (links.get(nagarik)!=null){
//                JSONArray newsContent = (JSONArray) links.get(nagarik);
//                news n1 = new news(newsContent.get(1).toString(),newsContent.get(0).toString(),nagarik);
//                items.add(newsContent.get(1).toString());
//                arrayListNews.add(n1);
//
//            }
//        }catch (JSONException e){
//            e.printStackTrace();
//        }



        CharSequence[] cs = items.toArray(new CharSequence[items.size()]);
        Log.d("data",cs.toString());
        ab.setItems(cs, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                 news n = arrayListNews.get(which);
                    Intent i = new Intent(Intent.ACTION_VIEW,Uri.parse(n.link));
                    mctx.startActivity(i);



            }
        });
        ab.create().show();


        return "check";
    }
}









