<script>
    import { Router, Link, Route } from "svelte-routing";
    import Home from './routes/Home.svelte';
    import Login from './routes/Login.svelte';
    import Profile from './routes/Profile.svelte';
</script>

<Router>
    <nav>
        <div class="left_div">
            <nav>
                <Link to="/home"  style="color:#00070F">CliniPet</Link>
            </nav>
        </div>
        
        <div class="right_div">
                <nav>
                    <Link to="/login" style="color:#00070F">Iniciar Sesión</Link>
                    &nbsp&nbsp;
                    <Link to="/profile" style="color:#00070F">Perfil</Link>
                </nav>
        </div>
    </nav>
    <Route path="/home" component={Home}/>
    <Route path="/login" component={Login}/>
    <Route path="/profile" component={Profile}/>
</Router>


<style>
    nav {
		display: flex;
	}
	nav div {
		flex: 1;
		padding: 1rem;
	}
    .left_div {
		text-align: left;
		background-color: #58e9ffb5;		
        font-weight: bolder;
	}
	.right_div {
		background-color: rgba(164, 161, 161, 0.292);        
        max-width: 181px;
        text-align: right;
        font-weight: bolder;
	}
</style>