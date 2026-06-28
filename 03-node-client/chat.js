const OLLAMA_URL = "http://localhost:11434/api/generate";

async function chat(prompt) {
    const response = await fetch(OLLAMA_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            model: "qwen3:14b",
            prompt: prompt,
            stream: false
        })
    });

    const data = await response.json();

    return data.response;
}


async function main() {

    const answer = await chat(
        "Explain Docker containers in simple words"
    );

    console.log("\nAI:");
    console.log(answer);
}


main();