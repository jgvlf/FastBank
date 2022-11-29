import React, {Children, Component, useState, useContext } from "react";
import { AuthContext } from '../../context/auth';
import { useNavigate } from 'react-router-dom';
import logo from "../../assets/img/Logo.png";
import HM from "../../assets/img/hamburger_menu.svg";
import { useEffect } from "react";

export function Header(){
    const [user, setUser] = useState({ cpf: ''});
    const { logout } = useContext(AuthContext);

    const [isConnected, setIsConnected] = useState(false);

    const navigate = useNavigate()

    useEffect(()=>{
        const _user = localStorage.getItem('user')
        if(!_user){
            setIsConnected(false);
        }
        if(_user){
            setUser(JSON.parse(_user))
            setIsConnected(true);
        }
    },[])

    const [active, setActive] = useState(false);
    const ToggleMode = () => {
        setActive(!active);
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        logout();
        navigate("/");
        location.reload();
    };

        return (
        <>
                <div className="z-[1000] px-[25px] justify-between flex h-[70px] w-screen fixed top-0 bg-[#002855] tablet:w-screen tablet:h-[100px] ">
                    <a href="/"><img className="h-[70px] tablet:w-[100px] tablet:h-[100px]" src={logo} alt="FastBank" /></a>
                    <div className={"items-center w-[70px] h-[70px] flex tablet:hidden"}>
                        <a href=""><img className="w-[50px] h-[50px]" src={HM} alt="Menu" /></a>
                    </div>
                    <ul className=" hidden tablet:flex tablet:items-center tablet:w-[70%] justify-around">
                        <div>
                            <a href="/"><li>Home</li></a>
                        </div>
                        <div>
                            <a href="#"><li>Recursos</li></a>
                        </div>
                        <div>
                            <a href="#"><li>Benefícios</li></a>
                        </div>
                        <div>
                            <a href="#"><li>Mímos</li></a>
                        </div>
                        <div>
                            <a href="#"> <li>Dúvidas</li></a>
                        </div>
                    </ul>
                    <div className="hidden tablet:w-[20%] tablet:flex tablet:items-center tablet:justify-around">
                        {!isConnected &&
                        <>
                            <ul>
                                <a href="/login"><li>Login</li></a>
                            </ul>
                            <ul>
                                <a href="/signup"><li>Signup</li></a>
                            </ul>
                        </>
                        }
                        {isConnected &&
                        <>
                            <ul className="w-full">
                                <h1><li>Bem Vindo {user.cpf}!</li></h1>
                            </ul>
                            <ul>
                                <button onClick={handleSubmit}><li>Logout</li></button>
                            </ul>
                        </>
                        }
                    </div>
                </div>
            </>
        );
    }