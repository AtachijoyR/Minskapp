<h1>Centro Veterinario CliniPet</h1>

<script lang="ts">
    import { 
        Image,
        Carousel,
        CarouselControl,
        CarouselIndicators,
        CarouselItem,
        CarouselCaption 
    } from 'sveltestrap';

    const items = [
        {
        url: 'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/Z2ZHWPOGBFAH7LPKCWLEU5XKCE.jpg',
        title: '',
        subTitle: ''
        },
        {
        url: 'https://smb.ibsrv.net/imageresizer/image/blog_images/1200x1200/23330/97482/0443241001547141937.jpg',
        title: '',
        subTitle: ''
        },
        {
        url: 'https://w0.peakpx.com/wallpaper/481/108/HD-wallpaper-happy-easter-rabbit-grass-easter-card-animal-cute-egg-green-bunny-rodent.jpg',
        title: '',
        subTitle: ''
        }
    ];
    let activeIndex = 0;
</script>
<div class="col-sm-6" style="width: 800px; margin-left: 50%; transform: translateX(-50%)">
    <Carousel {items} bind:activeIndex ride interval={2000}>
        <CarouselIndicators bind:activeIndex {items} />
            <div class="carousel-inner">
            {#each items as item, index}
                <CarouselItem bind:activeIndex itemIndex={index}>
                <img src={item.url} class="d-block w-100" alt={item.title} />
                </CarouselItem>
            {/each}
            </div>
        <CarouselControl direction="prev" bind:activeIndex {items} />
        <CarouselControl direction="next" bind:activeIndex {items} />
    </Carousel>
</div>

<!--
<div class="card-deck text-center">
    <div class="card">
      <Image src="https://cloudfront-us-east-1.images.arcpublishing.com/infobae/Z2ZHWPOGBFAH7LPKCWLEU5XKCE.jpg"></Image>
      <div class="card-body">
        <p class="card-text">Para buscar a una mascota en los registros clínicos seleccione:</p>
      </div>
    </div>
    <div class="card">
      <Image src="https://smb.ibsrv.net/imageresizer/image/blog_images/1200x1200/23330/97482/0443241001547141937.jpg"></Image>
      <div class="card-body">
        <p class="card-text">Para registrar una nueva mascota seleccione:</p>
      </div>
    </div>
</div>
--->
<style>
    :global(body){
        background-image: url("https://cdn.discordapp.com/attachments/982444201558020116/988260548690976828/IMG_3446.png");
    }
    h1 {
		color: #32C2C8;
		text-transform: uppercase;
		font-size: 3em;
        text-align: center;
	}         
</style>
