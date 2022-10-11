import React, {Component} from "react";
import logo from "../assets/img/Logo.png";
import HM from "../assets/img/hamburger_menu.svg"

class Header extends Component {
    render() { 
        return (
        <>
                <div className="z-[1000] px-[25px] justify-between flex h-[70px] w-screen fixed top-0 bg-[#002855] tablet:w-screen tablet:h-[100px] ">
                    <a href="#"><img className="h-[70px] tablet:w-[100px] tablet:h-[100px]" src={logo} alt="FastBank" /></a>
                    <div className="items-center w-[70px] h-[70px] flex tablet:hidden">
                        <a href=""><img className="w-[50px] h-[50px]" src={HM} alt="Menu" /></a>
                    </div>
                    <ul className=" hidden tablet:flex tablet:items-center tablet:w-[80%] justify-around">
                        <div>
                            <a href="#"><li>Home</li></a>
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
                    <div className="hidden tablet:w-[10%] tablet:flex tablet:items-center tablet:justify-around">
                        <ul>
                            <a href="#"><li>Login</li></a>
                        </ul>
                    </div>
                </div>
            </>
        );
    }
}
 
export default Header;