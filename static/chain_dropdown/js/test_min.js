console.log("active chain drop down")

console.log('main js activate')


// Just showing place data
const placeDataBox = document.getElementById('place-data-box')
$.ajax({
    type: 'GET',
    url: '/place_response/',
    success : function (response) {
        //console.log(response.data)
        const placeData = response.data
        //apply map for single item
        placeData.map(place_item=>{

            const car_option = document.createElement('div')
            car_option.textContent =place_item.place_name
            car_option.setAttribute('class','item')
            car_option.setAttribute('data-value',place_item.place_name)
            placeDataBox.appendChild(car_option) // sending the div

        })

    },
    error : function (error) {
        console.log(error)
    }
})





const  ratingDataBox = document.getElementById('raiting-data-box')
// getting hotel place id for get follow up the change element
const HotePlaceInput = document.getElementById('hotel_place_dropdown')
// if some thing change on Hote place dropdown
HotePlaceInput.addEventListener('change',place_event =>{
    console.log('hotel place change')
    const SelectHotelPlace = place_event.target.value
    console.log("value "+SelectHotelPlace)
    $.ajax({
        type    :'GET',
        url     :'/rating_response/',
        data    :{data:SelectHotelPlace},
        success :function (response) {
            ratingDataBox.innerHTML='';
            console.log(response.data)
            ratingData = response.data

            ratingData.map(rating_item=>{

            const rating_option = document.createElement('div')
            rating_option.textContent =rating_item
            rating_option.setAttribute('class','item')
            rating_option.setAttribute('data-value',rating_item)
            ratingDataBox.appendChild(rating_option) // sending the div

        })
        },
        error   :function (error) {
            console.log(error)
        }
    })
})


//getting data from rating data box it
// if some thing change on rating data box the value will sent to back-end
const  HotelNameDataBox = document.getElementById('hotelName-data-box')
// getting hotel place id for get follow up the change element
const ratingInput = document.getElementById('raiting_dropdown')
// if some thing change on rating place dropdown

ratingInput.addEventListener('change',rating_event =>{
    console.log('hotel place change')
    const SelectHotelPlace = rating_event.target.value
    console.log("value "+SelectHotelPlace)
    $.ajax({
        type    :'GET',
        url     :'/name_response/',
        data    :{data:SelectHotelPlace},
        success :function (response) {

            console.log(response.data)
            ratingData = response.data
            ratingData.map(name_item=>{
            const name_option = document.createElement('div')
            name_option.textContent =name_item
            name_option.setAttribute('class','item')
            name_option.setAttribute('data-value',name_item)
            HotelNameDataBox.appendChild(name_option) // sending the div

        })

        },
        error   :function (error) {
            console.log(error)
        }
    })

})

//getting data from name data box it
// if some thing change on name data box the value will sent to back-end
const  categoryDataBox = document.getElementById('category-data-box')
const nameInput = document.getElementById('hotelName_dropdown')
nameInput.addEventListener('change',catagory_event =>{
    console.log('hotel catagory change change')
    const SelectHotelcatagory = catagory_event.target.value
    console.log("value "+SelectHotelcatagory)
    $.ajax({
        type    :'GET',
        url     :'/catagory_response/',
        data    :{data:SelectHotelcatagory},
        success :function (response) {
            ratingData = response.data
            ratingData.map(catagory_item=>{
            const catagory_option = document.createElement('div')
            catagory_option.textContent =catagory_item
            catagory_option.setAttribute('class','item')
            catagory_option.setAttribute('data-value',catagory_item)
            categoryDataBox.appendChild(catagory_option) // sending the div

        })

        },
        error   :function (error) {
            console.log(error)
        }
    })

})