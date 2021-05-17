import React, { useEffect, useState } from 'react';
import {NavLink, useParams} from 'react-router-dom';
import './CSS/SearchResults.css'


function Search() {
    const [artists, setArtists] = useState([]);
    const { searchInput } = useParams();
    console.log(searchInput)
    useEffect(() => {
        async function fetchData() {
            const response = await fetch('/api/artists/');
            const responseData = await response.json();
            setArtists(responseData.artists);
        }
        fetchData();
    }, []);
    
    let searchResults;
    artists.map((artist) => {
        if (artist.name.toLowerCase().includes(searchInput.toLowerCase())) {
        console.log(artist.name)
            searchResults = (
            <li key={artist.id}>
                <NavLink to={`/artists/${artist.id}`}>{artist.name}</NavLink>
            </li>
            )
        } 
    })

    return (
        <div>
            <h1 id='resultsText'>Search Results:</h1>
            <ul className='searchResults'>{searchResults}</ul>
        </div>
    )
}

export default Search;