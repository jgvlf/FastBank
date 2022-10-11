import React, { useEffect, useState} from "react";
import axios from 'axios';


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
        <div className=" mt-[70px] w-screen h-full bg-[#023E7D] mobileS:h-screen default:w-screen default:h-screen">
            {clients.map((client)=>
            <div key={client.id}>
                <h1>{client.last_name}</h1>
                <h1>{client.first_name}</h1>
            </div>
            )}
        </div>
     );
}

export default Body;