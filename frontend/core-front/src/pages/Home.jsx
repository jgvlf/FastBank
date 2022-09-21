import React, {Component} from "react";
import Header from '../components/Header';
import Footer from '../components/Footer';
import Body from '../components/Body';

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