// source
const sourceDataBox = document.getElementById('source-data-box')
$.ajax({
    type: 'GET',
    url: '/source_reponse/',
    success : function (response) {
        const sourceData = response.data
        sourceData.map(item=>{
            const option = document.createElement('div')
            option.textContent =item
            option.setAttribute('class','item')
            option.setAttribute('data-value',item)
            sourceDataBox.appendChild(option) // sending the div

        })

    },
    error : function (error) {
        console.log(error)
    }
})

//destination
const destinationDataBox = document.getElementById('destination-data-box')


$.ajax({
    type: 'GET',
    url: '/destination_reponse/',
    success : function (response) {
        const destinationData = response.data
        destinationData.map(item=>{
            const option = document.createElement('div')
            option.textContent =item
            option.setAttribute('class','item')
            option.setAttribute('data-value',item)
            destinationDataBox.appendChild(option) // sending the div

        })

    },
    error : function (error) {
        console.log(error)
    }
})


// SOURCE  AND DESTINATION FORM SENDING BACKE-END!
const routeDatabox = document.getElementById('route-data-box')
function SourceDestionSubmission(event) {
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
              url    : '/route_reponse_data',
              data   :{body},
              success:function (response) {
                  console.log(response.data)
                  const routeData = response.data
                  console.log(routeData)
                  //Food_coast_Show_id.innerText = costData
                  routeData.map(item=>{

                    const option = document.createElement('div')
                    option.textContent =item
                    option.setAttribute('class','item')
                    option.setAttribute('data-value',item)
                    routeDatabox.appendChild(option) // sending the div

                })


              },
              error  : function (error) {
                  console.log(error)
              }
          })

}

$("#source_and_destination_id").submit(SourceDestionSubmission)


// if some thing chnage on route drop down
const  mooddataBox = document.getElementById('travell-mood-data-box')
const routeInpute = document.getElementById('route_dropdown')
routeInpute.addEventListener('change',event =>{
    console.log('hotel place change')
    const SelectedData = event.target.value
    console.log("value "+SelectedData)
    $.ajax({
        type    :'GET',
        url     :'/mood_reponse/',
        data    :{data:SelectedData},
        success :function (response) {
            console.log(response.data)
            moodData = response.data
            moodData.map(item=>{
                const option = document.createElement('div')
                option.textContent =item
                option.setAttribute('class','item')
                option.setAttribute('data-value',item)
                mooddataBox.appendChild(option) // sending the div

        })
        },
        error   :function (error) {
            console.log(error)
        }
    })
})


// if some thing change on mood drop down
const  classdataBox = document.getElementById('vehicle-class-data-box')
const moodInpute = document.getElementById('travell_mode_dropdown')
moodInpute.addEventListener('change',event =>{
    console.log('hotel place change')
    const SelectedData = event.target.value
    console.log("value "+SelectedData)
    $.ajax({
        type    :'GET',
        url     :'/class_reponse/',
        data    :{data:SelectedData},
        success :function (response) {
            console.log(response.data)
            classData = response.data
            classData.map(item=>{
                const option = document.createElement('div')
                option.textContent =item
                option.setAttribute('class','item')
                option.setAttribute('data-value',item)
                classdataBox.appendChild(option) // sending the div

        })
        },
        error   :function (error) {
            console.log(error)
        }
    })
})


// if some thing change on class drop down
const  companynamedataBox = document.getElementById('company-names-data-box')
const classInpute = document.getElementById('vehicle_class_dropdown')
classInpute.addEventListener('change',event =>{
    const SelectedData = event.target.value
    console.log("value "+SelectedData)
    $.ajax({
        type    :'GET',
        url     :'/company_name_reponse/',
        data    :{data:SelectedData},
        success :function (response) {
            console.log(response.data)
            companyNameData = response.data
            companyNameData.map(item=>{
                const option = document.createElement('div')
                option.textContent =item
                option.setAttribute('class','item')
                option.setAttribute('data-value',item)
                companynamedataBox.appendChild(option) // sending the div

        })
        },
        error   :function (error) {
            console.log(error)
        }
    })
})


const  comfortdataBox = document.getElementById('vechile-comfort-data-box')
const vechileNameInpute = document.getElementById('company_names_dropdown')
vechileNameInpute.addEventListener('change',event =>{
    const SelectedData = event.target.value
    console.log("value "+SelectedData)
    $.ajax({
        type    :'GET',
        url     :'/vechile_comfort_reponse/',
        data    :{data:SelectedData},
        success :function (response) {
            console.log(response.data)
            comfortNameData = response.data
            comfortNameData.map(item=>{
                const option = document.createElement('div')
                option.textContent =item
                option.setAttribute('class','item')
                option.setAttribute('data-value',item)
                comfortdataBox.appendChild(option) // sending the div

        })
        },
        error   :function (error) {
            console.log(error)
        }
    })
})