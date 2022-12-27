/**
 * @file stats.h
 * @author duyanwei (duyanwei0702@gmail.com)
 * @brief
 * @version 0.1
 * @date 2022-12-04
 *
 * @copyright Copyright (c) 2022
 *
 */

#ifndef DSO_STATS_H_
#define DSO_STATS_H_

#include <iomanip>
#include <ostream>
#include <string>

#include "util/timer.h"

namespace dso
{
/**
 * @brief
 *
 */
struct TrackingLog
{
    double timestamp = 0.0;
    double tracking  = 0.0;

    double make_image = 0.0;

    double coarse_tracking    = 0.0;
    int    num_points         = 0;
    int    num_levels         = 0;
    int    num_opt_iterations = 0;

    double coarse_tracing = 0.0;
    int    num_traces     = 0;

    /**
     * @brief Set the Zero object
     *
     */
    void reset()
    {
        *this = TrackingLog();
    }

    /**
     * @brief
     *
     * @param os
     * @param l
     * @return std::ostream&
     */
    friend std::ostream& operator<<(std::ostream& os, const TrackingLog& l)
    {
        os << std::setprecision(20);
        os << l.timestamp << " ";
        os << std::setprecision(6);
        os << l.tracking << " " << l.make_image << " " << l.coarse_tracking
           << " " << l.num_points << " " << l.num_levels << " "
           << l.num_opt_iterations << " " << l.coarse_tracing << " "
           << l.num_traces << "\n";
        return os;
    }

    /**
     * @brief Get the Header object
     *
     * @return std::string
     */
    static std::string getHeader()
    {
        return "# timestamp tracking make_image coarse_tracking num_points "
               "num_levels num_opt_iterations coarse_tracing num_traces\n";
    }
};

/**
 * @brief
 *
 */
struct MappingLog
{
    double timestamp = 0.0;
    double mapping   = 0.0;

    double activate_points      = 0.0;
    int    num_activated_points = 0;

    double optimization       = 0.0;
    int    num_keyframes      = 0;
    int    num_points         = 0;
    int    num_opt_iterations = 0;

    double remove_outliers = 0.0;
    int    num_outliers    = 0;

    double make_new_traces = 0.0;
    int    num_new_traces  = 0;

    double marginalize_frame = 0.0;

    /**
     * @brief Set the Zero object
     *
     */
    void reset()
    {
        *this = MappingLog();
    }

    /**
     * @brief
     *
     * @param os
     * @param l
     * @return std::ostream&
     */
    friend std::ostream& operator<<(std::ostream& os, const MappingLog& m)
    {
        os << std::setprecision(20);
        os << m.timestamp << " ";
        os << std::setprecision(6);
        os << m.mapping << " " << m.activate_points << " "
           << m.num_activated_points << " " << m.optimization << " "
           << m.num_keyframes << " " << m.num_points << " "
           << m.num_opt_iterations << " " << m.remove_outliers << " "
           << m.num_outliers << " " << m.make_new_traces << " "
           << m.num_new_traces << " " << m.marginalize_frame << "\n";
        return os;
    }

    /**
     * @brief Get the Header object
     *
     * @return std::string
     */
    static std::string getHeader()
    {
        return "# timestamp mapping activate_points num_activated_points "
               "optimization num_keyframes num_points num_opt_iterations "
               "remove_outliers num_outliers make_new_traces num_new_traces "
               "marginalize_frame\n";
    }
};

using TicTocTimer = slam_utility::stats::TicTocTimer;

}  // namespace dso

#endif  // DSO_STATS_H_