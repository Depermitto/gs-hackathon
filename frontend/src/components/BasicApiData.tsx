import React from "react";


const BasicApiData = () => {
    const [data, setData] = React.useState<any>(null);

    React.useEffect(() => {
        fetch("http://localhost:8000")
            .then((res) => res.json())
            .then((data) => setData(data));
    }, []);

    return (
        <div>
            {data ? (
                <div>
                    <h1>{data.title}</h1>
                    <p>{data.message}</p>
                </div>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default BasicApiData;