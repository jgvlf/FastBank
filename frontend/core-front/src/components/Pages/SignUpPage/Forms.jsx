import React, { useState, useContext } from "react";
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../../../context/auth';

export function Forms(props){
    const { cadastrar } = useContext(AuthContext);

    const [cpf, setCpf] = useState('');
    const [password, setPassword] = useState('');

    const navigate = useNavigate();

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log("submit", { cpf, password });
        cadastrar(cpf, password);
    };

    return(
        <div className="flex w-full h-full items-center justify-center">
            <div className="w-[250px] h-auto bg-white border-2 rounded-[20px] border-transparent">
            <h1 className="text-black flex justify-center">SignUp</h1>
                <div className="flex w-full h-full items-center justify-center">
                    <form id="login" method="post">
                        <label htmlFor="flcpf" className="text-black">CPF:</label><br />
                        <input type="text" name="fcpf" id="fcpf" onChange={(event)=>setCpf(event.target.value)} className="w-full text-black border-2 rounded border-black"/><br />
                        <label htmlFor="flpassword" className="text-black">Password:</label><br />
                        <input type="password" name="fpassword" id="fpassword" onChange={(event)=>setPassword(event.target.value)} className="text-black font-[Arial] border-2 rounded border-black"/>
                        <div className="my-[20px] flex justify-center border-2 rounded border-black">
                            <button className="w-[168px] h-[30px] text-black" type="submit" form="login" onClick={handleSubmit}>SignUp</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}