import React from "react";
import { Header } from "../components/Standard/Header";
import { Footer } from "../components/Standard/Footer";
import { SignUpMainPage } from "../components/Pages/SignUpPage/SignUpMainPage";


export function SignUpPage(){
    return(
        <div className="w-screen h-screen">
            <Header/>
            <SignUpMainPage/>
            <Footer/>
        </div>
    )
}