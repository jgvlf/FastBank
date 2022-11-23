import {createBrowserRouter} from 'react-router-dom';
import { HomePage } from '../pages/HomePage';
import { SignInPage } from '../pages/SignInPage';

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
        ])
    )
}