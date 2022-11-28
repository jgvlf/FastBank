import { createBrowserRouter, BrowserRouter as Router, Route, Routes, Navigate, } from 'react-router-dom';
import { HomePage } from '../pages/HomePage';
import { SignInPage } from '../pages/SignInPage';
import { SignUpPage } from '../pages/SignUpPage';
import { AuthProvider, AuthContext } from '../context/auth';


export function router(){
    return(
        createBrowserRouter([
            {
                path:"/",
                element: <HomePage/>
            },
            {
                path:"/login",
                element: <SignInPage/>
            },
            {
                path:"/signup",
                element: <SignUpPage/>
            },
        ])
    )
}