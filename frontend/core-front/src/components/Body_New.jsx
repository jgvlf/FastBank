import React, { useEffect, useState} from "react";
import axios from 'axios';
import FastEffectImg from '../assets/img/fast_effect_001.png';
import ThunderEffectImg from '../assets/img/thunder_effect_001.png';


function Body() {
    const [clients, setClients] = useState([]);

    const fetchData = async () => {
        const {data} = await axios.get('http://127.0.0.1:8000/api/clientes/')
        setClients(data);
    }

    useEffect(()=>{
        fetchData();
    }, [])

    return ( 
        <div className="mt-[70px] w-screen bg-[#023E7D] mobileS:h-screen default:w-screen default:h-screen default:mt-[100px]">
            <div className="inline-block w-screen">
                <div className="absolute fast-effect"></div>
                <div className="relative bg-[url('../assets/img/thunder_effect_001.png')]"></div>
            </div>
            {clients.map((client)=>
            <div className="px-[20px] pt[10px]" key={client.id}>
                <h1>{client.last_name}</h1>
                <h1>{client.first_name}</h1>
            </div>
            )}
        </div>
     );
}

export default Body;