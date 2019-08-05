package com.roguragain.myapplication;

import android.content.Context;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.List;




public class newsAdapter extends ArrayAdapter<news> {
    public newsAdapter(@NonNull Context context, List<news> objects) {
        super(context, 0, objects);
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {

        View listItemView = convertView;
        if(listItemView == null){
            listItemView = LayoutInflater.from(getContext()).inflate(R.layout.news,parent,false);

        }

        news ne = getItem(position);

        TextView text = listItemView.findViewById(R.id.title);
        text.setText(ne.news);

        return  listItemView;
    }
}
