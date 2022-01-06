console.log("main js activate")



//form id
const sourceFormID = document.getElementById('form-source-id')
const destinationFormID = document.getElementById('form-destination-id')


//showing///////////source data
// get data from back-end and show one front-end via ajax
const sourceDataBox = document.getElementById('source-data-box');
$.ajax({

    type   :'GET',
    url    : '/source_json_res/',
    success: function (response) {
        const SourceData = response.data

        SourceData.map(data_items=>{ //apply operation to each data item
            //creating div for drop down value
            const option = document.createElement('div')
            option.textContent =data_items
            option.setAttribute('class','item')
            option.setAttribute('data-value',data_items)
            sourceDataBox.appendChild(option) // sending the div
        })
    },
    error  : function (error) {
        console.log(error)
    }
})


////sending source data///
const sourceInput = document.getElementById('source_dropdown')
// if some thing change on the drop down box
sourceInput.addEventListener('change',events=>{
    console.log('source box data change')
    // get the selected value
    const selectedSource = events.target.value
    // sending the value to back-end via ajax
    $.ajax({
        type    :'GET',
        url     :'/avalable_route/',
        data    :{selectedSource:selectedSource},
        success :function (response) {
            console.log(response)


            // button wiil pops up while clicking the destination box
            // if some thing change on destination box
            destinationInput.addEventListener('change',e=>{
                btnBox.classList.remove('not-visible')
            })

        },
        error   :function (error) {
            console.log(error)
        }


    })


})








//showing data
////////////////////////////////////destination data box///////////////////////////
const destinationDataBox = document.getElementById('destination-data-box');
$.ajax({

    type   :'GET',
    url    :'/destination_json_res/',
    success: function (response) {
        const destinationData = response.data

        destinationData.map(data_items=>{ //apply operation to each data item
            //creating div for drop down value
            const option = document.createElement('div')
            option.textContent =data_items
            option.setAttribute('class','item')
            option.setAttribute('data-value',data_items)
            destinationDataBox.appendChild(option) // sending the div
        })
    },
    error  : function (error) {
        console.log(error)
    }
})


// a button will visible if the destination box is selected
const btnBox = document.getElementById('btn-box')

//get selected destination drop down value
const destinationInput = document.getElementById('destination_dropdown')

const routeDataBox = document.getElementById('route-data-box');
// if some thing change on the drop down box
destinationInput.addEventListener('change',event=>{
    console.log('destnation data change box data change')
    const selectedDestination = event.target.value
    console.log("selectedDestination:",selectedDestination)

    $.ajax({
        type : 'GET',
        url :"/avalable_route/",
        data: {
            selectedDestination: selectedDestination,

        },
        success:function (response) {
            // console.log(response.data)
            const routedata = response.data
            $(routeDataBox).html("")
            $('#route_dropdown .text').text('');
            routedata.map(data_item=>{
                const option = document.createElement('div')
                option.textContent =data_item
                option.setAttribute('class','item')
                option.setAttribute('data-value',data_item)
                routeDataBox.appendChild(option)

            })




        },
        error : function (error) {
            console.log(error)
        }
    })


})



//////////////Route  response boxes
//lets grab the route value from the route drop-down-box
const routeInput = document.getElementById('route_dropdown')

routeInput.addEventListener('change',event=>{
    console.log("route box change")
    const selectRoute = event.target.value
    console.log('route selected:',selectRoute)

    $.ajax({
        type    :'GET',
        url     :"/reoute_response/",
        data    :{
            selectedRoute:selectRoute,
        }
        ,
        success :function (response) {
            console.log("Back-end reponse",response.data)
        },
        error   : function (error) {
            console.log(error)
        }
    })

})




// form submission

sourceFormID.addEventListener('submit',e=>{
    e.preventDefault()
    console.log('submitted')
})

destinationFormID.addEventListener('submit',e=>{
    e.preventDefault()
    console.log('submitted')
})




