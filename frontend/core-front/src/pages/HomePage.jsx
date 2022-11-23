import React, {Component} from "react";
import { Header } from '../components/Standard/Header';
import { Footer } from '../components/Standard/Footer';
import Body from '../components/Pages/HomePage/Body';

export function HomePage(){
    return (
        <div className='w-screen h-screen'>
            <Header />

            <Body />

            <Footer />
        </div>  
    );
}