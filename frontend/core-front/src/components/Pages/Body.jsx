import React, { useEffect, useState} from "react";
import axios from 'axios';
import FastEffectImg from '../../assets/img/fast_effect_001.png';
import ThunderEffectImg from '../../assets/img/thunder_effect_001_inverted.png';


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
        <div className="mt-[70px] w-screen h-full bg-[#023E7D] default:w-screen default:h-screen default:mt-[100px]">
                <div style={{backgroundImage: `url(${FastEffectImg})`}} className="z-[0] bg-center bg-no-repeat bg-cover w-screen h-full default:w-screen default:h-full  ">
                    <div style={{backgroundImage: `url(${ThunderEffectImg})`}} className="z-[1] bg-center bg-no-repeat bg-auto w-screen h-full left-[100px]
                    default:w-full default:h-screen default:bg-cover default:bg-[top_right_-300px]">
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