
const ADD_TRANS = "songStorage/ADD_TRANS"
const GET_TRANS = "songStorage/GET_TRANS"
const ADD_COMMENT = "songStorage/ADD_COMMENT"
const GET_COMMENT = "songStorage/GET_COMMENT"


const addTrans = (trans) => ({
    type: ADD_TRANS,
    payload: trans
})


const getTrans = (trans) => ({
    type: GET_TRANS,
    payload: trans
})

const addComment= (comment) => ({
    type: ADD_COMMENT,
    payload: comment
})


const getComment = (comment) => ({
    type: GET_COMMENT,
    payload: comment
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
    // return newTranslation;
}

export const getTranslation = (songId) => async (dispatch) => {
    const response = await fetch(`/api/translations/${songId.songId}`);
    console.log(response);
    const responseData = await response.json();
    dispatch(getTrans(responseData))
    return responseData;
}


export const createComment = ({ comment, userId, songId }) => async (dispatch) => {
    const response = await fetch("/api/comments/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            comment,
            userId,
            songId
        }),
    });
    const newComment = await response.json();
    dispatch(addComment(newComment))
    // return newComment;
}

export const getComments = (songId) => async (dispatch) => {
    const response = await fetch(`/api/comments/${songId.songId}`);
    console.log(response);
    const responseData = await response.json();
    dispatch(getComment(responseData))
    return responseData;
}



export default function songStorage(state = {}, action) {
    let newState
    switch (action.type) {
        case ADD_TRANS:
            newState = Object.assign({}, state)
            newState.trans = [...state.translation, action.payload]
            return newState
        case GET_TRANS:
            newState = { ...state, ...action.payload }
            return newState
        case ADD_COMMENT:
            newState = Object.assign({}, state)
            newState.comment = [...state.comment, action.payload]
            return newState
        case GET_COMMENT:
            newState = {...state, ...action.payload}
            return newState
        default:
            return state;
    }
}