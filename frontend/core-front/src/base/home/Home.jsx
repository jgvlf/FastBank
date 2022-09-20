import React, {Component} from "react";
import Header from './header/Header';
import Footer from './footer/Footer';
import Body from './body/Body';

class Home extends Component {
    state = {  } 
    render() { 
        return (
            <div className='w-screen h-screen'>
                <Header />

                <Body />

                <Footer />
            </div>  
        );
    }
}
 
export default Home;