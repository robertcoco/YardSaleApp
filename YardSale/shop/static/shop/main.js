const menuEmail = document.querySelector(".navbar-email");
const shopMenuIcon = document.querySelector(".navbar-shopping-cart");
//const productDetailIcon = document.querySelector(".product-detail-close");

const desktopMenu = document.querySelector(".desktop-menu");
const menuMobile = document.querySelector(".mobile-menu");
const buttonMenuMobile = document.querySelector(".menu");
const shopCartMenu = document.querySelector("#shoppingCart");
const cardsContainer = document.querySelector(".cards-container");
const productDetail = document.querySelector("#productDetail");

menuEmail.addEventListener("click", toggleDesktopMenu);
buttonMenuMobile.addEventListener("click", toggleMobileMenu);
shopMenuIcon.addEventListener("click", toggleshopCartMenuMenu);

//productDetailIcon.addEventListener("click", closeProductDetail);

function toggleDesktopMenu() {
    desktopMenu.classList.toggle("inactive");
    const isShoppingCartClosed = shopCartMenu.classList.contains("inactive");

    if (!isShoppingCartClosed) {
        shopCartMenu.classList.add("inactive");
    }
}

function toggleMobileMenu() {
    menuMobile.classList.toggle("inactive");

    const isShoppingCartClosed = shopCartMenu.classList.contains("inactive");
    if (!isShoppingCartClosed) {
        shopCartMenu.classList.add("inactive");
    }
}

function toggleshopCartMenuMenu(){
    const isMobileMenuClosed = menuMobile.classList.contains("inactive");
    const isDesktopMenuClosed = desktopMenu.classList.contains("inactive")
    // close the mobile menu when you click the shoppingCartIcon and open the shopCartMenu.
    // in order to open one we need to close the last one.
    if (!isMobileMenuClosed) {
        menuMobile.classList.add("inactive");
    }

    if (!isDesktopMenuClosed) {
        desktopMenu.classList.add("inactive");
    }

    shopCartMenu.classList.toggle("inactive");

}

// function openProductDetail() {
//     const isProductDetailClosed = productDetail.classList.contains("inactive");
//     const isShopCartMenuOpened = !shopCartMenu.classList.contains("inactive");

//     if (!isProductDetailClosed) {
//         productDetail.classList.add("inactive");
//     }

//     if (isShopCartMenuOpened) {
//         shopCartMenu.classList.add("inactive");
//     }

//     productDetail.classList.remove("inactive");
// }

// function closeProductDetail() {
//     productDetail.classList.add("inactive");
// }

// get the products from an external api.
// async function getProduct() 
// {
//   let response = await fetch(`https://fakestoreapi.com/products`);
//   let data = await response.json();
//   console.log(data)
//   //renderProducts(data);
//   return data;
// }

// const productList = getProduct();
// console.log(productList)

// render the products in the web page.
// function renderProducts(arr) {
//     for (product of arr) {
//         // product = {product.name, produtc.price}
//         const productCard = document.createElement("div");
//         productCard.classList.add("product-card");
    
//         const productInfo = document.createElement("div");
//         productInfo.classList.add("product-info");
        
//         const productImg = document.createElement("img");
//         productImg.setAttribute("src", product.image);
//         productImg.addEventListener("click", openProductDetail);
        
//         const productInfoDiv = document.createElement("div");
        
//         const productPrice = document.createElement("p");
//         productPrice.innerHTML = "$" + product.price;
        
//         const productName = document.createElement("p");
//         productName.innerHTML = "$" + product.title;
        
//         const buttonImgCart = document.createElement("button")
//         const productImgCart = document.createElement("img");
//         const productFigure = document.createElement("figure");
//         productImgCart.setAttribute("src", "https://cdn-icons-png.flaticon.com/512/3523/3523885.png" );
//         buttonImgCart.appendChild(productImgCart)
//         productFigure.appendChild(buttonImgCart);
//         productInfoDiv.appendChild(productName);
//         productInfoDiv.appendChild(productPrice);
        
//         productInfo.appendChild(productInfoDiv);
//         productInfo.appendChild(productFigure);
    
//         productCard.appendChild(productImg);
//         productCard.appendChild(productInfo);
    
//         cardsContainer.appendChild(productCard);
        
//     }
// }


