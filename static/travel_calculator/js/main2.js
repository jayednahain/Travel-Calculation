console.log("active min2")



//avalable route response showing
// const sourceDataBox = document.getElementById('source-data-box');
// $.ajax({
//
//     type   :'GET',
//     url    : '/source_json_res/',
//     success: function (response) {
//         const SourceData = response.data
//
//         SourceData.map(data_items=>{ //apply operation to each data item
//             //creating div for drop down value
//             const option = document.createElement('div')
//             option.textContent =data_items
//             option.setAttribute('class','item')
//             option.setAttribute('data-value',data_items)
//             sourceDataBox.appendChild(option) // sending the div
//         })
//     },
//     error  : function (error) {
//         console.log(error)
//     }
// })



// if something is change on route change data box

// const routeInput = document.getElementById('route_dropdown')
// // if some thing change on the drop down box
// routeInput.addEventListener('change',events=>{
//
//     console.log('route box data change')
//     // get the selected value
//     const selectedSource = events.target.value
//     // sending the value to back-end via ajax
//     $.ajax({
//         type    :'GET',
//         url     :'/avalable_route/',
//         data    :{selectedSource:selectedSource},
//         success :function (response) {
//             console.log(response)
//
//
//             // button wiil pops up while clicking the destination box
//             // if some thing change on destination box
//             destinationInput.addEventListener('change',e=>{
//                 btnBox.classList.remove('not-visible')
//             })
//         },
//         error   :function (error) {
//             console.log(error)
//         }
//     })
// })


// const routeInput = document.getElementById('route_dropdown')
// // if some thing change on the drop down box
// routeInput.addEventListener('change',events=>{
//
//     console.log('route box data change')
//     // get the selected value
//     const selectedSource = events.target.value
//     // sending the value to back-end via ajax
//     $.ajax({
//         type    :'GET',
//         url     :'/avalable_route/',
//         data    :{selectedSource:selectedSource},
//         success :function (response) {
//             console.log(response)
//
//
//             // button wiil pops up while clicking the destination box
//             // if some thing change on destination box
//             destinationInput.addEventListener('change',e=>{
//                 btnBox.classList.remove('not-visible')
//             })
//         },
//         error   :function (error) {
//             console.log(error)
//         }
//     })
// })



var test_array = []
var test_2 = [1,2,3]
document.querySelectorAll('.route').forEach(item => {
  item.addEventListener('change', event_data => {


      test_array.push(event_data.target.value)
      console.log("hellow")
      //console.log(test_array.length)
      if (test_array.length < 2)
      {
          console.log("low")
      }
      else{
          //test_array.push(event_data.target.value)
          console.log(test_array)
          $.ajax({
              type   : 'GET',
              url    : '/take_two_test/',
              data   :{
                  data:test_array[0],
                  data2:"hellow",
                  data3:test_2[0]
              },
              success:function (response) {
                  console.log(response.data)

              },
              error  : function (error) {
                  console.log(error)
              }
          })




      }




  })
})






