import React, {Component} from "react";
import Header from '../components/Standard/Header';
import Footer from '../components/Standard/Footer';
import Body from '../components/Pages/Body';

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