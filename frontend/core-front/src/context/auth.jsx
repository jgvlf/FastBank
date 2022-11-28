import React, { createContext, useState, useEffect } from 'react';

import { useNavigate } from 'react-router-dom';

import { createUser, logar } from "../api/api";

export const AuthContext = createContext();

export const AuthProvider = ({children}) => {
  
  const navigate = useNavigate();
  
  const [user, setUser] = useState(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const recoveryUser = localStorage.getItem('user');
    const token = localStorage.getItem('token');

    if(recoveryUser && token){ setUser(recoveryUser); }

    setLoading(false);

  }, []);

  const login = async (cpf, password) => {

    const res = await logar(""+cpf, ""+password);

    const response = {'cpf': res.data.cpf,'password':res.data.password,'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXNzYWdlIjoiSldUIFJ1bGVzISIsImlhdCI6MTQ1OTQ0ODExOSwiZXhwIjoxNDU5NDU0NTE5fQ.-yIVBD5b73C75osbmwwshQNRC7frWUYrqaTjTpza2y4'};

    const loggedUser = {'cpf':response.cpf, 'password':response.password};
    const token = response.token; 

    localStorage.setItem("user", loggedUser);
    localStorage.setItem("token", token);

    setUser(loggedUser);

    navigate('/');
    
  };

  const logout = () => {

    localStorage.removeItem('user');
    localStorage.removeItem('token');

    setUser(null);

    navigate('/login');

  };

  const cadastrar = async (cpf, password) => {
  
      const res = await createUser(""+cpf, ""+password);
  
      const response = res.status;
      
      if(response === 200){
        alert("Conta cadastrada com sucesso!");
      
      }else{
        alert("Error status: "+response)
      }
      
    };
  
  return(
    <AuthContext.Provider value={{authenticated: !!user, user, loading, login, logout, cadastrar}}>
      {children}  
    </AuthContext.Provider>
  );

}