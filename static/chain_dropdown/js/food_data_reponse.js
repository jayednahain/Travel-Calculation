

// showing food place data
const foodplaceDataBox = document.getElementById('food-place-box')
$.ajax({
    type: 'GET',
    url: '/food_place_reponse/',
    success : function (response) {
        const foodplaceData = response.data
        foodplaceData.map(place_item=>{
            const food_place_option = document.createElement('div')
            food_place_option.textContent =place_item.place_name
            food_place_option.setAttribute('class','item')
            food_place_option.setAttribute('data-value',place_item.place_name)
            foodplaceDataBox.appendChild(food_place_option) // sending the div

        })

    },
    error : function (error) {
        console.log(error)
    }
})


const  foodresturantdatabox = document.getElementById('resturent-name-data-box')
const foodPlaceInput = document.getElementById('food_place_dropdown')
foodPlaceInput.addEventListener('change',place_event =>{
    const SelectResturentlPlace = place_event.target.value

    $.ajax({
        type    :'GET',
        url     :'/food_resturant_name_response/',
        data    :{data:SelectResturentlPlace},
        success :function (response) {
            foodresturantdatabox.innerHTML='';
            foodresturantdata = response.data
            foodresturantdata.map(resturant_food_item=>{
            const food_returant_option = document.createElement('div')
            food_returant_option.textContent =resturant_food_item
            food_returant_option.setAttribute('class','item')
            food_returant_option.setAttribute('data-value',resturant_food_item)
            foodresturantdatabox.appendChild(food_returant_option)
        })
        },
        error   :function (error) {
            console.log(error)
        }
    })
})

const  foodTypedatabox = document.getElementById('foodtype-data-box')
const resturentNameInput = document.getElementById('resturent_name_dropdown')
resturentNameInput.addEventListener('change',name_event =>{
    const SelectName = name_event.target.value
    $.ajax({
        type    :'GET',
        url     :'/food_type_reponse/',
        data    :{data:SelectName},
        success :function (response) {
            foodTypedatabox.innerHTML='';
            food_type_data = response.data
            food_type_data.map(food_type_item=>{
            const food_type_option = document.createElement('div')
            food_type_option.textContent =food_type_item
            food_type_option.setAttribute('class','item')
            food_type_option.setAttribute('data-value',food_type_item)
            foodTypedatabox.appendChild(food_type_option) // sending the div

        })
        },
        error   :function (error) {
            console.log(error)
        }
    })
})


const  foodNamedatabox = document.getElementById('item-name-data-box')
const foodTypeInput = document.getElementById('food_type_dropdown')
foodTypeInput.addEventListener('change',name_event =>{
    const SelectType = name_event.target.value
    $.ajax({
        type    :'GET',
        url     :'/item_name_reponse/',
        data    :{data:SelectType},
        success :function (response) {
            foodNamedatabox.innerHTML='';
            console.log(response.data)
            item_name_data = response.data
            item_name_data.map(food_type_item=>{
            const food_type_option = document.createElement('div')
            food_type_option.textContent =food_type_item
            food_type_option.setAttribute('class','item')
            food_type_option.setAttribute('data-value',food_type_item)
            foodNamedatabox.appendChild(food_type_option) // sending the div

        })
         },
        error   :function (error) {
            console.log(error)
        }
    })
})
