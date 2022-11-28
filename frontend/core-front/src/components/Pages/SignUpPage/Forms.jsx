import React from "react";

export function Forms(props){
    return(
        <div className="flex w-full h-full items-center justify-center">
            <div className="w-[250px] h-auto bg-white border-2 rounded-[20px] border-transparent">
            <h1 className="text-black flex justify-center">SignUp</h1>
                <div className="flex w-full h-full items-center justify-center">
                    <form id="login" method="post">
                        <label htmlFor="flcpf" className="text-black">CPF:</label><br />
                        <input type="text" name="fcpf" id="fcpf" className="text-black border-2 rounded border-black"/><br />
                        <label htmlFor="flpassword" className="text-black">Password:</label><br />
                        <input type="password" name="fpassword" id="fpassword" className="text-black border-2 rounded border-black"/>
                        <div className="my-[20px] flex justify-center border-2 rounded border-black">
                            <button className="w-[168px] h-[30px] text-black" type="submit" form="login" onClick={()=>{}}>Login</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}