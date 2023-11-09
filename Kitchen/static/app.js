// Initialize an array with zeros to represent the quantities of each menu item
const quantities = [0, 0, 0, 0, 0, 0];

function addToCart(pizzaName, pizzaPrice, itemIndex) {
    const cartList = document.getElementById('cart-list');
    const cartTitle = document.getElementById('cart-title');
    
    // Check if the item already exists in the cart
    let itemExists = false;
    const cartItems = cartList.children;
    
    for (let i = 0; i < cartItems.length; i++) {
        const item = cartItems[i];
        if (item.textContent.includes(pizzaName)) {
            itemExists = true;
            const itemText = item.textContent;
            const quantity = parseInt(itemText.split(' x ')[1]);
            item.textContent = `${pizzaName} x ${quantity + 1}`;
            // Update the quantities array when adding to the cart
            quantities[itemIndex] = quantity + 1;
        }
    }
    
    if (!itemExists) {
        // Create a new list item to represent the selected pizza in the cart
        const cartItem = document.createElement('li');
        cartItem.textContent = `${pizzaName} x 1`;
        cartList.appendChild(cartItem);
        // Update the quantities array when adding to the cart
        quantities[itemIndex] = 1;
    }
    
    // Calculate the total price based on the prices of items in the cart
    const cartItemsList = cartList.children;
    let total = 0;
    
    for (let i = 0; i < cartItemsList.length; i++) {
        const item = cartItemsList[i];
        const itemText = item.textContent;
        const itemPrice = parseFloat(itemText.split(' x ')[1]) * parseFloat(pizzaPrice.replace('€', ''));
        total += itemPrice;
    }
    
    // Update the cart title and the total price
    cartTitle.textContent = '';
    const orderTotal = document.querySelector('.orderprice');
    
    // Check if the cart is empty, and display "Cart is Empty" if so
    if (cartItemsList.length > 0) {
        orderTotal.textContent = `€${total.toFixed(2)}`;
    } else {
        orderTotal.textContent = "Cart is Empty";
    }
}

function markOrderAsDone() {
    // Create an order data object or array
    const orderData = {
        quantities: quantities, // The quantities array that represents menu items
        // You can add more order-related information here if needed
    };

    // Send the order data to the server using an AJAX request
    fetch('/complete_order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(orderData), // Convert the order data to JSON
    })
    .then(response => response.json())
    .then(data => {
        // Handle the server's response if needed
        console.log(data.message);
        // You can update the user interface to indicate that the order is processed.
    });
}
