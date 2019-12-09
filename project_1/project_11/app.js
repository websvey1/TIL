const app = new Vue({
	el: "#app",
	data: {
		logo: 'MO<i class="fab fa-vuejs"></i>IE',
		isMain: true,
		genres: [],
		movies: [],
		detailView: false,
		movieDetail: {
			newScoreContent: '',
			newScoreScore: '',
		},
	},
	methods: {
		toggleDetail: function (id = null) { 
			if (id) {
				const movie = this.movies[id - 1] 

				this.movieDetail.title = movie.title
				this.movieDetail.audience = movie.audience
				this.movieDetail.poster_url = movie.poster_url
				this.movieDetail.description = movie.description

				this.movieDetail.reviews = movie.score_set


				const scoreList = movie.score_set
				const onlyScore = []
				scoreList.forEach((score) => onlyScore.push(score.score))
				this.movieDetail.scores = Number((onlyScore.reduce((total, x) => total += x, 0) / onlyScore.length).toFixed(2)) 
				this.movieDetail.genre = '' 

				this.movieDetail.id = id
			}
			this.detailView = !this.detailView
		},
		getMovies: function () {
			axios.get('https://django-intro-websvey1.c9users.io/api/v1/movies/')
				.then(response => response.data)
				.then(movies => {
					this.movies = movies.map(movie => {
						return {
							...movie,
							newScoreContent: ''
						}
					})
				})
				.catch(error => console.log(error))
		},

		addScore: function (movie) {

			axios.post(`https://django-intro-websvey1.c9users.io/api/v1/movies/${movie.id}/scores/`, {content: movie.newScoreContent, score: movie.newScoreScore})
				.then(response => {
					alert(response.data.message)
					movie.reviews.push({content: movie.newScoreContent, score: movie.newScoreScore})
					movie.newScoreContent = ''
					movie.newScoreScore = ''
					const addedScore = []
					movie.reviews.forEach((score) => addedScore.push(Number(score.score)))
					movie.scores = Number((addedScore.reduce((total, x) => total += x, 0) / addedScore.length).toFixed(2))

				})
				.catch(error => console.log(error))
			// .then(addedScore => {
			// 	movie.score_set.push(addedScore)
			// })
		},
		getGenres: function () {
			axios.get('https://django-intro-websvey1.c9users.io/api/v1/genres/')
				.then(response => response.data)
				.then(genres => {
					this.genres = genres
				})
				.catch(error => console.log(error))
		},
		getScores: function () {

		}

	},
	mounted: function () {
		this.getMovies()
	},

	computed: {},

	watch: {},

	created: function () { 
		axios.get(`https://django-intro-websvey1.c9users.io/api/v1/genres`) 
			.then(res => this.genres = res.data)
	}
});