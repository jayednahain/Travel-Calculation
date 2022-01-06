console.log("ccccccc")


const route_cost_show = document.getElementById('cost_display')
function routecost(event) {


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
              url    : '/route_cost_response_data',
              data   :{body},
              success:function (response) {
                  // console.log(response.data)
                  const costData = response.data
                  route_cost_show.innerText = costData



              },
              error  : function (error) {
                  console.log(error)
              }
          })

}

$("#route_form_id").submit(routecost)
