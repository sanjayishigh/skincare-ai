let userSelections = {};

async function getRecommendations() {
    const age = document.getElementById('age').value;
    const skinType = document.getElementById('skinType').value;
    const concern = document.getElementById('concern').value;
    const productType = document.getElementById('productType').value;

    if (!age) {
        alert("Please enter your age.");
        return;
    }

    userSelections = { age, skin_type: skinType, concern, product_type: productType };

    document.getElementById('loading').classList.remove('hidden');
    document.getElementById('results').innerHTML = '';

    try {
        const response = await fetch('/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userSelections)
        });

        const data = await response.json();
        document.getElementById('loading').classList.add('hidden');
        const container = document.getElementById('results');

        if (!data.products || data.products.length === 0) {
            container.innerHTML = "<p class='no-results'>No specific matches found. Try changing the product type.</p>";
            return;
        }

        data.products.forEach(p => {
            const card = document.createElement('div');
            card.className = 'card';
            
            // Star rating generator
            const stars = "⭐".repeat(Math.round(p.rating));

            card.innerHTML = `
                <div class="card-header" style="background-color: #ffe5ec; padding: 10px;">
                    <img src="${p.image_url}" alt="${p.brand}" class="product-img">
                </div>
                <div class="card-body">
                    <h3>${p.brand}</h3>
                    <p class="p-type">${p.product_type}</p>
                    <div class="price-tag">₹${p.price}</div>
                    <div class="rating">${stars} (${p.rating}) • ${p.reviews} reviews</div>
                    <hr>
                    <p class="ingredients"><strong>Key:</strong> ${p.key_ingredient}</p>
                    <p class="ingredients"><strong>Plus:</strong> ${p.additional_ingredient}</p>
                    <button class="routine-btn" onclick='generateRoutine(${JSON.stringify(p).replace(/'/g, "&#39;")})'>Get Routine & Analysis</button>
                </div>
            `;
            container.appendChild(card);
        });

    } catch (error) {
        console.error(error);
        alert("Error connecting to server.");
        document.getElementById('loading').classList.add('hidden');
    }
}

async function generateRoutine(product) {
    const modal = document.getElementById('routineModal');
    const textDiv = document.getElementById('routineText');
    
    modal.classList.remove('hidden');
    textDiv.innerHTML = "<p>Consulting AI Dermatologist...</p>";

    try {
        const response = await fetch('/routine', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                skin_type: userSelections.skin_type,
                concern: userSelections.concern,
                product: product
            })
        });
        
        const data = await response.json();
        textDiv.innerHTML = data.routine ? marked.parse(data.routine) : "Error generating routine.";
        
    } catch (error) {
        textDiv.innerHTML = "Error: " + error.message;
    }
}

function closeModal() {
    document.getElementById('routineModal').classList.add('hidden');
}