import React from "react";
import { Header } from "../components/Standard/Header";
import { Footer } from "../components/Standard/Footer";
import { SignInMainPage } from "../components/Pages/SignInPage/SignInMainPage";


export function SignInPage(){
    return(
        <div className="w-screen h-screen">
            <Header/>
            <SignInMainPage/>
            <Footer/>
        </div>
    )
}