<script>
	import axios from 'axios';
	import { Styles } from 'sveltestrap';
	import {onMount} from 'svelte';
	import {
        Alert,
        Container,
        Button,
        Table,
    } from 'sveltestrap';
	let Animals = [];

	const getPets= () => {
		axios.get('http://127.0.0.1:8000/Listar-Mascotas/')
		.then(res =>{
			Animals = res.data;

			console.log(res);
		})
	}

	onMount(getPets);

</script>

<main>
	<Container>
	<h1> Svelte Axios </h1>
	<hr>

	{#await Animals}
		Loading...
	{:then Animals}
		<ul>
			{#each Animals as animal }
				<li>{animal.name}</li>
			{/each}

		</ul>
	{:catch error}
		{error}
	{/await}
	</Container>

</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>