// app/routes/api.genetic-algorithm.js

export async function loader() {
    const response = await fetch('http://localhost:5000/api/genetic-algorithm'); // Update with your Flask API URL in production
    if (!response.ok) {
        throw new Response('Failed to fetch data', { status: response.status });
    }
    return response.json();
}

export default function GeneticAlgorithm() {
    const data = useLoaderData();

    return (
        <div>
            <h1>Genetic Algorithm Result</h1>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );
}