import React, { useEffect, useState } from "react";
import Container from '@material-ui/core/Container';
import Navigation from "components/Navigation";
import Grid from '@material-ui/core/Grid';

const Landing = () => {
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchHelloWorld = async () => {
            const url = "/api/hello_world/";
            const options = {
                method: "GET",
                Accept: "application/json",
                "Content-Type": "application/json",
            };

            const response = await fetch(url, options);

            // Try catch because .json will throw if no data
            try {
            // This will extract the data and convert from a json string to an object
                const responseData = await response.json();
                if (response.ok) {
                    setData(responseData.message);
                } else {
                    setError(responseData);
                }
            } catch (e) {
                setError(e);
            }
        };
        fetchHelloWorld();
    }, []);

    const displayResults = () => (
        <div>{error ? `Error: ${error}` : `Data: ${data}`}</div>
    );

    return (
        <Container>
            <Navigation />
            {displayResults()}
        </Container>
    );
};

export default Landing;