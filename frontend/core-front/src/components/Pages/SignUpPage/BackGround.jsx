import React from "react";

export function BackGround({children}){
    return(
        <div className="mt-[70px] z-[0] bg-[#222d5a] w-full h-full 
         flex justify-center items-center relative">
            <div className="pt-[50px] pb-[150px] mobileS:px-[50px] w-screen h-screen">
                {children}
            </div>
        </div>
    )
}