export function getBadgeColor(status) {
    let badge = ''

    if (status === 'waiting')
        badge = 'bg-gradient-to-r from-yellow-500 via-orange-400 to-yellow-500 text-white'
    else if (status === 'at work')
        badge = 'bg-gradient-to-r from-cyan-500 via-blue-400 to-cyan-500 text-white'
    else if (status === 'completed')
        badge = 'bg-gradient-to-r from-lime-600 via-green-600 to-lime-600 text-white'
    else if (status === 'canceled')
        badge = 'bg-gradient-to-r from-orange-600 via-red-600 to-orange-600 text-white'
    else 
        badge = 'bg-gradient-to-r from-neutral-500 via-slate-600 to-neutral-500 text-white'

    return badge
}