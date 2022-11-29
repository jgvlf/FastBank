import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../../../context/auth';

export const Forms = ()=>{
    const { login } = useContext(AuthContext);

    const [cpf, setCpf] = useState('');
    const [password, setPassword] = useState('');

    const navigate = useNavigate();

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log("submit", { cpf, password });
        login(cpf, password);
    };

    const handleClick = (event) => {
        event.preventDefault();
        navigate('/signup');
    };

    return(
        <div id="login" className="flex w-full h-full items-center justify-center">
            <div className="w-[250px] h-auto bg-white border-2 rounded-[20px] border-transparent">
            <h1 className="text-black flex justify-center">Login</h1>
                <div className="flex w-full h-full items-center justify-center">
                    <form id="login">
                        <label htmlFor="flcpf" className="text-black">CPF:</label><br />
                        <input type="text" name="fcpf" id="fcpf" className="w-full text-black border-2 rounded border-black" onChange={(event)=>setCpf(event.target.value)}/><br />
                        <label htmlFor="flpassword" className="text-black">Password:</label><br />
                        <input type="password" name="fpassword" id="fpassword" className="text-black font-[Arial] border-2 rounded border-black" onChange={(event)=>setPassword(event.target.value)}/>
                        <div className="my-[20px] flex justify-center border-2 rounded border-black">
                            <button className="w-[168px] h-[30px] text-black" type="button" form="login" onClick={handleSubmit}>Login</button>
                        </div>
                        <div className="my-[20px] flex justify-center border-2 rounded border-black">
                            <button className="w-[168px] h-[30px] text-black" type="button" form="login" onClick={handleClick}>Click here to SignUp</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}