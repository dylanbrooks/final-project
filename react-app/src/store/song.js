
const ADD_TRANS = "songStorage/ADD_TRANS"
const GET_TRANS = "songStorage/GET_TRANS"
const SET_TRANS = "songStorage/SET_TRANS"


const addTrans = (trans) => ({
    type: ADD_TRANS,
    payload: trans
})


const getTrans = (trans) => ({
    type: GET_TRANS,
    payload: trans
})

const setTrans = (trans) => ({
    type: SET_TRANS,
    payload: trans
})


export const createTranslation = ({translation, startIndex, stopIndex, userId, songId}) => async (dispatch) => {
    const response = await fetch("/api/translations/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            translation,
            startIndex,
            stopIndex,
            userId,
            songId
        }),
    });
    const newTranslation = await response.json();
    dispatch(addTrans(newTranslation))
    return newTranslation;
}

export const getTranslation = (songId) => async (dispatch) => {
    const response = await fetch(`/api/translations/${songId.songId}`);
    console.log(response);
    const responseData = await response.json();
    dispatch(getTrans(responseData))
    return responseData;
}



export default function songStorage(state = {}, action) {
    let newState
    switch (action.type) {
        case ADD_TRANS:
            return action.payload;
        case GET_TRANS:
            newState = Object.assign({}, state)
            newState.trans = action.payload
            return newState
            // return { ...state, trans: action.payload };
        case SET_TRANS:
            return action.payload
        default:
            return state;
    }
}