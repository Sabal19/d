
const loginForm = document.getElementById('login-form')
const searchForm = document.getElementById('search-form')
const contentContainer = document.getElementById('content-container')
const baseEndpoint = "http://localhost:8000/api"
if (loginForm){


//handle this form
loginForm.addEventListener('submit',handleLogin)
searchForm.addEventListener('submit',handleSearch)
}

function handleSearch(event){

    event.preventDefault()
    let searchFOrmData = new FormData(searchForm)
    let searchObjectData = Object.fromEntries(searchFOrmData)
    let searchParams = new URLSearchParams(searchObjectData)
    const endpoint =`${baseEndpoint}/search/?${searchParams}`
    const headers ={"content-type":'application/json'}
    const authToken = localStorage.getItem('access')
    if(authToken){
        headers['Authorization'] = `Bearer ${authToken}`
    }

    const options = {
        method :"GET",
        headers:headers,
    }
    fetch(endpoint,options)  
    .then(response=>{
        console.log(response)
        return response.json
    })
    // .then( x=> {
    //     console.log(x)})
    .then(data=>{
        // console.log(data.hits)
        writeToContainer(data)
        const validData=isTokenNotValid(data)
        if(validData && contentContainer){
            contentContainer.innerHTML=""
            if(data && data.hits){
                let htmlStr = ""
                for(let result of data.hits){
                    htmlStr+= "<li>" + result.title+"</li>"
                }
                contentContainer.innerHTML= htmlStr
                if (data.hits.length ==0){
                    contentContainer.innerHTML="<p> No result found </p>"
                }
                

                }
            else {
                contentContainer.innerHTML="<p> No result found </p>"
            }
            }
        }
    )
    .catch(err=>{
        console.log('err',err)
    })
}
// function handleLogin(event){
//     console.log(event)

//     event.preventDefault()
//     const loginEndpoint =`${baseEndpoint}/token/`
//     let loginFOrmData = new FormData(loginForm)
//     let loginObjectData = Object.fromEntries(loginFOrmData)
//     let bodyStr = JSON.stringify(loginObjectData)
    
//     console.log(loginObjectData,bodyStr)

//     const options = {
//         method :"POST",
//         headers:{
//             "content-type":'application/json'
//         },
//         // body :""
//         body : bodyStr
//     }
//     fetch(loginEndpoint,options)  // request.posts || Promise
//     .then(response=>{
//         console.log(response)
//         return response.json
//     })
//     // .then( x=> {
//     //     console.log(x)})
//     .then(authData=>{
//         handleAuthData(authData,getProductList)
//     })
//     .catch(err=>{
//         console.log('err',err)
//     })
// }

function handleAuthData(authData,callback){
localStorage.setItem('access',authData.access)
localStorage.setItem('refresh',authData.refresh)
if(callback){
    callback()
}

}
function writeToContainer(data){
    if(contentContainer){
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data,null,4)+"</pre>"
    }
}

function getFetchOptions(method,body){
    return{
        
        method :method==null ? "GET":method, //if method is null put GET as default method else put the method which was passed
        headers:{
                "content-type":'application/json',
                "Authorization": `Bearer ${localStorage.getItem('access')}`
            },
            body : body?body:null
            // body : jsObject ? JSON.stringify(jsObject):null       // to use this put jsObject as parameter in the function
    
        }
    }
function isTokenNotValid(jsonData){
    if(jsonData.code && jsonData.code=="token_not_valid"){
        alert("Please Login Again")
        return false

    }
    return true
}
function validateJWTToken(){
    const endpoint = `${baseEndpoint}/token/verify`
    const options={
        method: "POST",
        headers : {
            "content-type" :'application/json'

        },
        body : JSON.stringify({
            token : localStorage.getItem("access")
        })
    }
    .fetch(endpoint,options)
    .then(response=>response.json())

}

function getProductList(){
    const endpoint =`${baseEndpoint}/products/`
    // const options = {
    //     method :"GET",
    //     headers:{
    //         "content-type":'application/json',
    //         "Authorization": `Bearer ${localStorage.getItem('access')}`
    //     },}  //This can be defined in the function as above 
    const options = getFetchOptions
    .fetch(endpoint,options)
    .then(response=>{
        console.log(response)
        return response.json()})
    .then(data=>{
    console.log(data)
    const validData = isTokenNotValid(data)
    if(validData){
    writeToContainer(data)}

    
})
}
validateJWTToken()

const searchClient = algoliasearch('UEEDA3M60W', '75bad7fa48d684052fca256fcebf5713');

const search = instantsearch({
  indexName: 'cfe_Product',
  searchClient,
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
  }),
  instantsearch.widgets.refinementList({
    container:"#user-lists",
    attribute: "user"
  }),
  instantsearch.widgets.refinementList({
    container:"#public-lists",
    attribute: "public"
  }),
  instantsearch.widgets.clearRefinements({
    container:"#clear-lists",
  }),
  instantsearch.widgets.hits({
    container: '#hits',
    templates :{
        // item : `<div>{{ title }}<p>{{ user }} </p> {{ price }}</div>`
        item : `<div>
        <div> {{#helpers.hilights}}{"attribute":"title"}{{/helpers.highlight}}
        <div> {{#helpers.hilights}}{"attribute":"body"}{{/elpers.highlight}}
        
        <p>{{ user }} </p> {{ price }}</div>`
    }
  })
]);

search.start();
