import React, { useContext } from 'react';

import { createBrowserRouter, BrowserRouter as Router, 
    Route,
    Routes, 
    Navigate, 
} from 'react-router-dom';

import { HomePage } from '../pages/HomePage';
import { SignInPage } from '../pages/SignInPage';
import { SignUpPage } from '../pages/SignUpPage';
import { AuthProvider, AuthContext } from '../context/auth';

const Private = ({children}) => {
  
    const { loading } = useContext(AuthContext);

    if(loading){
      return <div className='loading'>Carregando...</div>
    }

    const { authenticated } = useContext(AuthContext);

    if(!authenticated){
      return <Navigate to='/login' />
    }

    return children;

  };


export function Routers(){
    return(
        <Router>
            <AuthProvider>
                <Routes>
                    <Route exact path='/login' element={<SignInPage/>}/>
                    <Route exact path='/signup' element={<SignUpPage/>}/>
                    <Route exact path='/' element={
                        <Private>
                            <HomePage/>
                        </Private>
                    }/>
                </Routes>
            </AuthProvider>
        </Router>
        // createBrowserRouter([
        //     {
        //         path:"/",
        //         element: <HomePage/>
        //     },
        //     {s
        //         path:"/login",
        //         element: <SignInPage/>
        //     },
        //     {
        //         path:"/signup",
        //         element: <SignUpPage/>
        //     },
        // ])
    )
}