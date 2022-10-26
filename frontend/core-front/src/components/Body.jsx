import React, { useEffect, useState} from "react";
import axios from 'axios';
import FastEffectImg from '/fast_effect_001.png';
import ThunderEffectImg from '/thunder_effect_001_inverted.png';


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
        <div className="mt-[70px] w-screen h-auto bg-[#023E7D] default:w-screen default:h-screen default:mt-[100px]">
                <div style={{backgroundImage: `url(${FastEffectImg})`}} className="bg-center bg-no-repeat bg-cover w-screen min-h-[280px] h-[100vw] default:w-screen default:h-full  ">
                    <div style={{backgroundImage: `url(${ThunderEffectImg})`}} className="bg-[20px_center] bg-no-repeat bg-cover w-screen min-h-[280px] h-[100vw]
                    default:w-[983px] default:h-full default:inline-block default:float-right">
                        <div>

                        </div>
                    </div>
                
                {/* <div style={{backgroundImage: '../assets/img/fast_effect_001.png'}} className="">

                </div> */}
                {/* <img className="absolute w-screen h-[243px] bg-cover z-0 default:h-full" src={FastEffectImg} alt="" />
                <img className="relative w-screen h-[243px] bg-cover z-[900] scale-x-[-1] default:h-screen" src={ThunderEffectImg} alt="" /> */}
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