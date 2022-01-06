console.log('Connect Cost data!')


const hotel_cost_show_box = document.getElementById('hotel_cost_show_id')
function hoteldata(event) {
    event.preventDefault()
    const valuesInArray = $(this).serializeArray()
    console.log(valuesInArray)

    const body = {}


    //apply forEach loop
    valuesInArray.forEach(e =>{
        body[e.name] = e.value
    })

    console.log(valuesInArray)
    console.log(body)


    $.ajax({
              type   : 'GET',
              url    : '/hotel_cost_reponse',
              data   :{body},
              success:function (response) {
                  // console.log(response.data)
                  const costData = response.data
                  hotel_cost_show_box.innerText = costData



              },
              error  : function (error) {
                  console.log(error)
              }
          })

}

$("#hotel_form_id").submit(hoteldata)



const Food_coast_Show_id = document.getElementById('food_cost_show_id')
function foodCostData(event) {
    event.preventDefault()
    const valueArray = $(this).serializeArray()
    console.log(valueArray)

    const body = {}


    //apply forEach loop
    valueArray.forEach(e =>{
        body[e.name] = e.value
    })

    console.log(valueArray)
    console.log(body)


    $.ajax({
              type   : 'GET',
              url    : '/food_cost_response',
              data   :{body},
              success:function (response) {
                  // console.log(response.data)
                  const costData = response.data
                  Food_coast_Show_id.innerText = costData



              },
              error  : function (error) {
                  console.log(error)
              }
          })

}

$("#food_form_id").submit(foodCostData)



//const cost_btn_id = document.getElementById('route_cost_btn_id')
// console.log('cost 222 connect')
//
//
// $('#route_cost_btn_id').on('click', function (e){
//
//     e.preventDefault()
//
//     const source_id = document.getElementById('source').value
//     console.log(source_id)
//     const destination_id = document.getElementById('destination').value
//     const route_id = document.getElementById('route')
//     const travell_mood_id = document.getElementById('travell_mood').value
//     const vehicle_class_id = document.getElementById('vehicle_class').value
//     const company_names_id = document.getElementById('company_names').value
//     const vechile_comfort_id = document.getElementById('vechile_comfort').value
//     data = {
//         source_id : source_id,
//          destination_id :destination_id,
//          route_id:route_id,
//          travell_mood_id:travell_mood_id,
//          vehicle_class_id:vehicle_class_id,
//          company_names_id:company_names_id,
//          vechile_comfort_id:vechile_comfort_id
//     }
//      $.ajax({
//      type   : 'GET',
//      url    : '/route_cost_response_data',
//      data   :{data},
//      success:function (response) {
//                   // console.log(response.data)
//          const route_cost = response.data
//          console.log(route_cost)
//          //Food_coast_Show_id.innerText = costData
//
//      },
//      error  : function (error) {
//          console.log(error)
//      }
//  })
// })


