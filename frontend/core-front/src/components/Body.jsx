import React, {Component} from "react";


class Body extends Component {
    constructor(){
        super();
        this.state={
            data:[]
        };
    }

        async fetchData(){
            await fetch('http://127.0.0.1:8000/api/clientes/')
            .then(response=>response.json())
            .then((data)=>{
                this.setState({
                    data:data
                });
            });
        }

    componentDidMount(){
        this.fetchData();
    }
     
    render() {
        const empData = this.state.data;
        const rows = empData.map((emp)=>
            <div key={1}>
                <h1>{emp.last_name}</h1>
                <h1>{emp.first_name}</h1>
            </div>
        );  
        return (
            <>
                <div className=" mt-[70px] w-screen h-full bg-[#023E7D] mobileS:h-screen default:w-screen default:h-screen">
                    {rows}
                </div>

            </>
        );
    }
}
 
export default Body;