import React, {Component} from "react";

class Header extends Component {
    render() { 
        return (
            <>
                <div className="fixed top-0 w-screen h-[100px] bg-[#002855] default:w-screen default:h-[100px] mobileS:max-h-[40px]">
                </div>
            </>
        );
    }
}
 
export default Header;