import axios from 'axios';

export const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api/",
});

export const createUser = async(cpf, password) =>{
    let dados = {'cpf':cpf, 'password':password}
    return api.post('/usuarios/', dados)
}

export const logar = async(cpf, password) => {
    return api.get("/usuarios/" + cpf, { cpf, password } );
  };