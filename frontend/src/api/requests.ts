import axios from 'axios'

export const url = `/api/v1/`

export const getAllCars = async (query: string) => {
    const response = await axios.get(`${url}cars/${query}`)
    return response.data
}

export const createNewCar = async (payload: object) => {
    const response = await axios.post(`${url}cars/`, payload)
    return response.data
}

export const getOneCar = async (car_Id: number) => {
    const response = await axios.get(`${url}cars/${car_Id}`)
    return response.data
}

export const getAllOrders = async (query: string) => {
    const response = await axios.get(`${url}orders/${query}`)
    return response.data
}

export const createNewOrder = async (payload: object) => {
    const response = await axios.post(`${url}orders/`, payload)
    return response.data
}

export const getAllReviews = async (query: string) => {
    const response = await axios.get(`${url}reviews/${query}`)
    return response.data
}

export const createNewReview = async (payload: object) => {
    const response = await axios.post(`${url}reviews/`, payload)
    return response.data
}