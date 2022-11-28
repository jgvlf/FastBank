import React from "react";
import { BackGround } from "./BackGround";
import { Forms } from "./Forms";

export function SignUpMainPage(){
    return(
        <BackGround>
            <h1>SignUp</h1>
            <Forms/>
        </BackGround>
    )
}