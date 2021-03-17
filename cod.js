const API = require('call-of-duty-api')({ platform: "battle" });

function start(){
// try {
//     await API.login(, );
//  } catch(Error) {
//      //Handle Exception
//  }
API.FuzzySearch('leakycoax',"uno").then( data => {
try {
   console.log('result ' + data );
 } catch(Error) {
     //Handle Exception
 }
}
 );
try{
    console.log('true')
    console.log( API.login('LeakyCoax#2673265', ''))
    console.log('done')
   } catch(Error){
    console.log('login in error')
   }
try {
    let data = API.MWcombatwz('LeakyCoax#2673265', 'xbox');
    var elem = document.querySelector('.cod');
    elem.innerHTML = '<p>'+ data +'</p>';
 } catch(Error) {
     //Handle Exception
 }
}
start();